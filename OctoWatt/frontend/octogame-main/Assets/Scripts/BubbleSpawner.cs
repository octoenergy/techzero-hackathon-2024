using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class BubbleSpawner : MonoBehaviour
{
    public BubbleStation thisBubbleStation;
    public Bubble[] spawnerBubbles;
    private double accumulatedWeights;
    private System.Random rand = new System.Random();
    private float bubbleFrequency = 0.5f;

    private void Start()
    {


        foreach (Bubble bubble in spawnerBubbles)
        {
            

            if (bubble.Name == "red")
            {
                bubble.chance = thisBubbleStation.redBubblePercentage;
                Debug.Log("Red found!");
                Debug.Log("Bubble chance: " + bubble.chance);

            }

            if (bubble.Name == "green")
            {
                bubble.chance = thisBubbleStation.greenBubblePercentage;
                Debug.Log("green found!");
                Debug.Log("Bubble chance: " + bubble.chance);
            }

            if (bubble.Name == "normal")
            {
                bubble.chance = thisBubbleStation.normalBubblePercentage;
                Debug.Log("normal found!");
                Debug.Log("Bubble chance: " + bubble.chance);
            }
        }

        bubbleFrequency = thisBubbleStation.bubbleVolume;

        CalculateWeights();

        Debug.Log("Accumulated weights: " + accumulatedWeights);



        Debug.Log("Bubble Frequency: " + bubbleFrequency);

        /// assign bubble spawning settings
        InvokeRepeating("GenerateBubbles", 0.5f, bubbleFrequency);
    }


    private void GenerateBubbles()
    {
        /// change to random spawn on platform
        Vector3 randomSpawnPosition = this.transform.position + new Vector3(Random.Range(-1, 1), -4, 1);

        int bubbleIndex = GetRandomBubbleIndex();

        Bubble randomBubble = spawnerBubbles[bubbleIndex];

        GameObject generatedBubble = Instantiate(randomBubble.Prefab, randomSpawnPosition, Quaternion.identity);

        /// get bubble behaviour component
        BubbleBehaviour bubbleBehaviour = generatedBubble.GetComponent<BubbleBehaviour>();

        /// Assign attributes
        if (bubbleIndex == 0)
        {
            bubbleBehaviour.bubbleColour = "green";
        }
        else if (bubbleIndex == 1)
        {
            bubbleBehaviour.bubbleColour = "normal";
        }
        else if (bubbleIndex == 2)
        {
            bubbleBehaviour.bubbleColour = "red";
        }


        Debug.Log("Bubble Generated!");
    }


    private int GetRandomBubbleIndex()
    {
        double r = rand.NextDouble() * accumulatedWeights;

        for (int i = 0; i < spawnerBubbles.Length; i++)
            if (spawnerBubbles[i]._weight >= r)
                return i;

        return 0;
    }

    private void CalculateWeights()
    {
        accumulatedWeights = 0f;
        foreach (Bubble bubble in spawnerBubbles)
        {
            Debug.Log("Bubble weight to be added: " + bubble.chance);

            accumulatedWeights += bubble.chance;
            bubble._weight = accumulatedWeights;
        }
    }
}