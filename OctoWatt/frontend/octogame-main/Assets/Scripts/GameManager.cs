using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class GameManager : MonoBehaviour
{
    public BubbleStation morningBubbleStation;
    public BubbleStation afternoonBubbleStation;
    public BubbleStation eveningBubbleStation;
    public BubbleStation nighttimeBubbleStation;

    public float greenPoints = 0;
    public float normalPoints = 0;
    public float redPoints = 0;

    public int percentageGreen = 0;
    public TMP_Text scoreText;



    // Start is called before the first frame update
    void Awake()
    {


        /// load and process data from Octopus APIs for live status
        morningBubbleStation.bubbleStationName = "morning";
        morningBubbleStation.timeString = "7am to 12pm";
        morningBubbleStation.statusString = "Normal";
        morningBubbleStation.greenBubblePercentage = 20;
        morningBubbleStation.normalBubblePercentage = 70;
        morningBubbleStation.redBubblePercentage = 10;
        morningBubbleStation.bubbleVolume = 1.2f;

        afternoonBubbleStation.timeString = "12pm to 5pm";
        afternoonBubbleStation.statusString = "Normal";
        afternoonBubbleStation.greenBubblePercentage = 20;
        afternoonBubbleStation.normalBubblePercentage = 70;
        afternoonBubbleStation.redBubblePercentage = 10;
        afternoonBubbleStation.bubbleVolume = 1.4f;

        eveningBubbleStation.timeString = "5pm to 10pm";
        eveningBubbleStation.statusString = "Bad (Peak!)";
        eveningBubbleStation.greenBubblePercentage = 5;
        eveningBubbleStation.normalBubblePercentage = 10;
        eveningBubbleStation.redBubblePercentage = 85;
        eveningBubbleStation.bubbleVolume = 1.3f;

        nighttimeBubbleStation.timeString = "10pm to 3am";
        nighttimeBubbleStation.statusString = "Good (Windy!)";
        nighttimeBubbleStation.greenBubblePercentage = 75;
        nighttimeBubbleStation.normalBubblePercentage = 15;
        nighttimeBubbleStation.redBubblePercentage = 10;
        nighttimeBubbleStation.bubbleVolume = 0.9f;

    }

    // Update is called once per frame
    void Update()
    {
        

        if (greenPoints != 0 || normalPoints != 0 || redPoints != 0)
        {
            Debug.Log("Green points: " + greenPoints);
            Debug.Log("Normal points: " + normalPoints);
            Debug.Log("Red points: " + redPoints);


            percentageGreen = Mathf.RoundToInt(greenPoints / (greenPoints + normalPoints + redPoints) * 100);
            Debug.Log("Percentage Green: " + percentageGreen);

            scoreText.text = percentageGreen.ToString() + "%";
        }
        
    }
}
