using Newtonsoft.Json;
using System.Collections.Generic;
using UnityEngine;

public static class TradeManager
{
    private static string jsonFileRawTxt;

    public class Item
    {
        public string Name { get; set; }
        public int Buy { get; set; }
        public int Sell { get; set; }
    }

    public class Inventory
    {
        public string TradeType { get; set; }
        public List<Item> Items { get; set; }
    }

    public static List<Inventory> tradeInventory;

    public static Dictionary<string, Sprite> itemIconDict;
    public static Sprite iconWood;
    public static Sprite iconWool;

    public static void LoadData()
    {
        jsonFileRawTxt = Resources.Load<TextAsset>("Data/Trade").text;
        tradeInventory = JsonConvert.DeserializeObject<List<Inventory>>(jsonFileRawTxt);

        iconWood = Resources.Load<Sprite>("Images/Icon_Wood");
        iconWool = Resources.Load<Sprite>("Images/Icon_Wool");

        itemIconDict = new Dictionary<string, Sprite>() {
            {"Wood", iconWood },
            { "Wool", iconWool }
        };
    }

    public static Inventory GetTradeData(string tradeType)
    {
        if (tradeInventory == null) LoadData();
        foreach (Inventory inventory in tradeInventory)
        {
            if (inventory.TradeType == tradeType)
            {
                return inventory;
            }
        }
        Debug.LogError($"No trade type of type {tradeType} exists!");
        return null;
    }
}
