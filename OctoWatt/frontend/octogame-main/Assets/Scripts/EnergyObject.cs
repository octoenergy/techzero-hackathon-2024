using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnergyObject : MonoBehaviour
{
    public bool objectReleased = false;

    // Update is called once per frame
    void Update()
    {
        if (objectReleased == true)
        {
            Debug.Log("Moving object....");
            transform.position = Vector2.Lerp(transform.position, new Vector2(transform.position.x, -5), 1f * Time.deltaTime);
        }
    }

    public void TriggerDrop()
    {
        objectReleased = true;
    }
}


