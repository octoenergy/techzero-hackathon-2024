import mongoose, { Document, Model } from "mongoose";

enum DnoSubstationStatusEnum {
  GREEN = "green",
  AMBER = "amber",
  RED = "red",
}

enum TenureEnum {
  LEASEHOLD = "leasehold",
  FREEHOLD = "freehold",
}

export interface Property {
  _id: any;
  uprn: string;
  address_1: string;
  address_2: string;
  address_3: string;
  postcode: string;
  asset_rating: number;
  asset_rating_band: string;
  floor_area: number;
  building_level: number;
  main_heating_fuel: string;
  title_number: string;
  tenure: TenureEnum;
  company_registration_number: string;
  total_roof_surface_area: number;
  annual_energy_usage: number;
  latitude: number;
  longitude: number;
  building_emissions: number;
  yield_potential: number;
  dno_substation_status: DnoSubstationStatusEnum;
  potential_energy_savings: number;
  industry: string;
  optimal_generation: number;
  optimal_capacity: number;
  optimal_savings: number;
  company_name: string;
}

export interface PropertyDocument extends Property, Document {
  createdAt: Date;
  updatedAt: Date;
}

const propertySchema = new mongoose.Schema<PropertyDocument>(
  {
    uprn: {
      type: String,
      required: false,
    },
    address_1: {
      type: String,
      required: false,
    },
    address_2: {
      type: String,
      required: false,
    },
    address_3: {
      type: String,
      required: false,
    },
    postcode: {
      type: String,
      required: false,
    },
    asset_rating: {
      type: Number,
      required: false,
    },
    asset_rating_band: {
      type: String,
      required: false,
    },
    floor_area: {
      type: Number,
      required: false,
    },
    building_level: {
      type: Number,
      required: false,
    },
    main_heating_fuel: {
      type: String,
      required: false,
    },
    title_number: {
      type: String,
      required: false,
    },
    tenure: {
      type: String,
      required: false,
    },
    company_registration_number: {
      type: String,
      required: false,
    },
    total_roof_surface_area: {
      type: Number,
      required: false,
    },
    annual_energy_usage: {
      type: Number,
      required: false,
    },
    latitude: {
      type: Number,
      required: false,
    },
    longitude: {
      type: Number,
      required: false,
    },
    building_emissions: {
      type: Number,
      required: false,
    },
    yield_potential: {
      type: Number,
      required: false,
    },
    industry: {
      type: String,
      required: false,
    },
    optimal_capacity: {
      type: Number,
      required: false,
    },
    optimal_generation: {
      type: Number,
      required: false,
    },
    optimal_savings: {
      type: Number,
      required: false,
    },
    company_name: {
      type: String,
      required: false,
    },
  },
  {
    timestamps: true,
  }
);

const PropertyModel: Model<PropertyDocument> =
  mongoose.models?.properties || mongoose.model("properties", propertySchema);

export default PropertyModel;
