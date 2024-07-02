using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Octopus : MonoBehaviour
{
    public float moveSpeed;
    private float speedX, speedY;
    private Rigidbody2D octoBody;
    private GameManager gameManager;
    public EnergyObject energyObject;
    public GameObject tenticle;

    private void Awake()
    {
        gameManager = FindObjectOfType<GameManager>();
    }

    // Start is called before the first frame update
    void Start()
    {
        octoBody = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        speedX = Input.GetAxisRaw("Horizontal") * moveSpeed;
        speedY = Input.GetAxisRaw("Vertical") * moveSpeed;
        octoBody.velocity = new Vector2(speedX, speedY);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        Debug.Log("Bubble Triggered");

        /// capture bubble object

        BubbleBehaviour burstBubble = collision.gameObject.GetComponent<BubbleBehaviour>();

        /// process score
        string burstBubbleSize = burstBubble.bubbleSize;

        /// trigger score event

        float scoreToAdd;

        if (burstBubbleSize == "small")
        {
            scoreToAdd = 1;
        }
        else if (burstBubbleSize == "medium")
        {
            scoreToAdd = 3;
        }
        else
        {
            scoreToAdd = 5;
        }


        if (burstBubble.bubbleColour == "green")
        {
            gameManager.greenPoints += scoreToAdd;
        }
        else if (burstBubble.bubbleColour == "normal")
        {
            gameManager.normalPoints += scoreToAdd;
        }
        else
        {
            gameManager.redPoints += scoreToAdd;
        }

        /// trigger burst effect

        burstBubble.BurstBubble();

        /// Check if charge complete

        if (energyObject.objectReleased == false & (gameManager.greenPoints + gameManager.normalPoints + gameManager.redPoints) > 80)
        {
            Debug.Log("Object charged!");
            tenticle.SetActive(false);
            energyObject.TriggerDrop();

        }
    }
}
