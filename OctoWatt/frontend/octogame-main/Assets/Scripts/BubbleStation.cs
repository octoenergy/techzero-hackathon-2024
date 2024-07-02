using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class BubbleStation : MonoBehaviour
{
    public string bubbleStationName;
    public string timeString;
    public string statusString;
    public float greenBubblePercentage;
    public float normalBubblePercentage;
    public float redBubblePercentage;
    public float bubbleVolume;
    public Sprite correctSprite;

    public bool isActive = true;

    public SpriteRenderer stationSprite;
    public Collider2D stationCollider;
    public BubbleSpawner thisStationSpawner;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        /// capture falling object

        if (collision.gameObject.GetComponent<EnergyObject>() != null)
        {
            EnergyObject fallingObject = collision.gameObject.GetComponent<EnergyObject>();
            Destroy(fallingObject.gameObject, 1f);

            ///

            stationSprite.sprite = correctSprite;
        }

        
    }




}

