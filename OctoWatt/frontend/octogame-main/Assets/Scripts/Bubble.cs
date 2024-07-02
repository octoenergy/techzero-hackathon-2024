using UnityEngine;

[System.Serializable]
public class Bubble
{
    public string Name;

    public GameObject Prefab;

    [Range(0f, 100f)] public float chance = 100f;

    [HideInInspector] public double _weight;
}
