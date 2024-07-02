using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class BubbleBehaviour : MonoBehaviour
{
    public string bubbleSize = "small";
    public string bubbleColour;
    public SpriteRenderer bubbleSprite;
    public Collider2D bubbleCollider;
    public bool isActive;
    public Rigidbody2D bubbleBody;
    public Transform bubbleTransform;
    public Sprite burstSprite;

    private void Awake()
    {
        /// Get collider

        bubbleCollider = GetComponent<Collider2D>();
        bubbleSprite = GetComponent<SpriteRenderer>();

        /// Randomise bubble attributes

        bubbleBody.drag = bubbleBody.drag + Random.Range(1, 3);

        int sizeChoice = Random.Range(0, 3);

        if (sizeChoice == 0)
        {
            bubbleSize = "small";
        }
        else if (sizeChoice == 1)
        {
            bubbleTransform.localScale += new Vector3(0.5f, 0.5f, 0.5f);
            bubbleSize = "medium";
        }
        else if (sizeChoice == 2)
        {
            bubbleTransform.localScale += new Vector3(1f, 1f, 1f);
            bubbleSize = "large";
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (this.transform.position.y > 6)
        {
            Destroy(this.gameObject);
        }
    }

    /// burst bubble

    public void BurstBubble()
    {
        /// trigger sound
        bubbleSprite.sprite = burstSprite;

        Destroy(this.gameObject, 1f);
    }
}