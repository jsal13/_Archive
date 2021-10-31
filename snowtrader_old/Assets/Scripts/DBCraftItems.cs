using System.Collections.Generic;
using UnityEngine;

public static class DBCraftItems
{
    public class CraftItem
    {
        public string name;
        public int cost;
        public Sprite sprite;
        public GameObject objectPrefab;

        public CraftItem(string name, int cost, Sprite sprite, GameObject objectPrefab)
        {
            this.name = name;
            this.cost = cost;
            this.sprite = sprite;
            this.objectPrefab = objectPrefab;
        }
    }

    public static List<CraftItem> craftItems = null;

    public static List<CraftItem> GetCraftItemData()
    {
        if (craftItems == null)
        {
            craftItems = new List<CraftItem>
            {
                new CraftItem(
                name: "Bonfire",
                cost: 4,
                sprite: Resources.Load<Sprite>("Images/Crafting/Obj_Bonfire"),
                objectPrefab: Resources.Load<GameObject>("Prefabs/Obj_Bonfire")
            ),

                new CraftItem(
                name: "Leanto",
                cost: 25,
                sprite: Resources.Load<Sprite>("Images/Crafting/Obj_Leanto"),
                objectPrefab: Resources.Load<GameObject>("Prefabs/Obj_Leanto")
            )
            };
        }

        return craftItems;
    }


}