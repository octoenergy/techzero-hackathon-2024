import React, { useEffect, useRef, useState } from "react";
import mapboxgl from "mapbox-gl";

// Replace 'your_mapbox_access_token' with your actual Mapbox access token
mapboxgl.accessToken =
  "pk.eyJ1Ijoiam9uZXM1ODEiLCJhIjoiY2xwNzM4Y3JpMXZ1NjJrcWswNDFrbnl1ZiJ9.Ud2Oqbe9kgEmB3U3UOH98w";

interface MapProps {
  updateOption1: (newValue: number) => void;
}

const MapboxMap: React.FC<MapProps> = ({ updateOption1 }) => {
  const mapContainerRef = useRef<HTMLDivElement | null>(null);
  const [selectedBuildings, setSelectedBuildings] = useState<string[]>([]); // State to track list of selected buildings
  const [calculatingSolar, setCalculatingSolar] = useState(false); // State to control popup display
  const [currentValue, setCurrentValue] = useState<number>(30); // Initial value for newValue

  useEffect(() => {
    if (mapContainerRef.current) {
      const map = new mapboxgl.Map({
        container: mapContainerRef.current,
        style: "mapbox://styles/mapbox/streets-v11", // Style of the map
        center: [-1.2982167, 50.7029], // Initial map center in [lng, lat]
        zoom: 18, // Initial zoom level
      });

      map.on("load", () => {
        // Load GeoJSON file
        fetch("/buildings.geojson")
          .then((response) => response.json())
          .then((data) => {
            // Add GeoJSON data as a source
            map.addSource("custom-data", {
              type: "geojson",
              data: data,
            });

            // Add a layer to display the building GeoJSON data as 3D extrusions
            map.addLayer({
              id: "custom-layer",
              type: "fill-extrusion",
              source: "custom-data",
              paint: {
                // Use a property-driven color expression
                "fill-extrusion-color": [
                  "case",
                  ["in", ["get", "osm_id"], ["literal", selectedBuildings]],
                  "green",
                  "red",
                ],
                "fill-extrusion-height": 5, // Height of the building
                "fill-extrusion-base": 0, // Base height of the building
                "fill-extrusion-opacity": 0.6, // Opacity of the building
              },
            });

            // Add click event listener to toggle building color
            map.on("click", "custom-layer", (e) => {
              const features = map.queryRenderedFeatures(e.point, {
                layers: ["custom-layer"],
              });

              if (!features.length) {
                return;
              }

              // Simulate calculating solar potential
              setCalculatingSolar(true);
              const randomValue = Math.floor(2 + Math.random() * 4);
              const newValue = currentValue + 2 * randomValue;
              setCurrentValue(newValue);
              updateOption1(newValue);
              setTimeout(() => {
                setCalculatingSolar(false);
              }, 2000);

              const clickedFeature = features[0];
              const clickedBuildingId = clickedFeature?.properties?.osm_id;

              // Update selected buildings state
              setSelectedBuildings((prevSelectedBuildings) => {
                if (prevSelectedBuildings.includes(clickedBuildingId)) {
                  // Deselect the building if it's already selected
                  return prevSelectedBuildings.filter(
                    (id) => id !== clickedBuildingId,
                  );
                } else {
                  // Select the building if it's not selected
                  return [...prevSelectedBuildings, clickedBuildingId];
                }
              });
            });
          })
          .catch((error) => {
            console.error("Error loading GeoJSON:", error);
          });
      });

      // Clean up on unmount
      return () => map.remove();
    }
  }, [selectedBuildings, currentValue]); // Include currentValue in dependencies to trigger map layer repaint

  return (
    <>
      <div ref={mapContainerRef} style={{ width: "100%", height: "400px" }} />
      {calculatingSolar && (
        <div className="popup absolute left-0 top-20 z-40 h-[100%] w-[100%] bg-white">
          <p className="h-[100%] w-[100%] py-10 text-center text-2xl font-bold text-black">
            Calculating solar potential...
          </p>
        </div>
      )}
    </>
  );
};

export default MapboxMap;
