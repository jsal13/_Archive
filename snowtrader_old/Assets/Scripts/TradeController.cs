using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class TradeController : MonoBehaviour
{
    private GameObject tradingCanvas;
    private GameObject itemPrefab;
    private GameObject currentSelectionOutline;
    private TradeManager.Inventory traderInventory;
    private int currentCursorIDX = 0;
    private int currentCursorIDY = 0;
    [SerializeField] private TradeManager.Item currentSelectedItem; 
    private bool currentlyTrading = false;
    private readonly int initX = -90;
    private readonly int initY = 10;
    private readonly int itemWidth = 60;
    private readonly int itemHeight = 60;
    private readonly int maxItemsPerRow = 3;

    public delegate void PlayerEndedTrading();
    public static event PlayerEndedTrading OnPlayerEndedTrading;


    private void Awake()
    {
        tradingCanvas = GameObject.Find(DBHierarchyAddr.tradingCanvas);
        itemPrefab = Resources.Load<GameObject>("Prefabs/TradeItem");
        currentSelectionOutline = GameObject.Find(DBHierarchyAddr.tradingCurrentSelection);
        tradingCanvas = GameObject.Find(DBHierarchyAddr.tradingCanvas);
    }

    private void Start()
    {
        tradingCanvas.SetActive(false);
        TradeManager.LoadData();
    }

    private void Update()
    {
        if (currentlyTrading)
        {
            var dpad = GameManager.gamepad.dpad;
            // Move Selection
            if (dpad.down.wasPressedThisFrame) MoveSelection(0, 1);
            else if (dpad.up.wasPressedThisFrame) MoveSelection(0, -1);
            else if (dpad.left.wasPressedThisFrame) MoveSelection(-1, 0);
            else if (dpad.right.wasPressedThisFrame) MoveSelection(1, 0);
            // Buy-Sell
            else if (GameManager.gamepad.leftTrigger.wasPressedThisFrame) BuyItem();
            else if (GameManager.gamepad.rightTrigger.wasPressedThisFrame) SellItem();
            else if (GameManager.gamepad.bButton.wasPressedThisFrame) EndTrade();
        }
    }

    private void OnEnable()
    {
        PlayerTalk.OnPlayerStartedTrading += HandlePlayerStartedTrading;
    }

    private void OnDisable()
    {
        PlayerTalk.OnPlayerStartedTrading -= HandlePlayerStartedTrading;
    }

    private void HandlePlayerStartedTrading(bool value, GameObject target)
    {
        traderInventory = TradeManager.GetTradeData(target.GetComponent<CharacterInformation>().tradeType);

        currentlyTrading = true;
        tradingCanvas.SetActive(true);
        PopulateTradeDialog();
    }

    private void EndTrade()
    {
        OnPlayerEndedTrading?.Invoke();
        currentlyTrading = false;
        currentCursorIDX = 0;
        currentCursorIDY = 0;
        tradingCanvas.SetActive(false);
}

    private void PopulateTradeDialog()
    {
        int x = -90;
        int y = 10;
        int xAcc = 0;
        int yAcc = 0;

        foreach (TradeManager.Item item in traderInventory.Items)
        {
            GameObject obj = Instantiate(itemPrefab, new Vector3(0, 0, 0), Quaternion.identity);
            obj.transform.SetParent(tradingCanvas.transform, false) ;
            Vector3 offset = new Vector3(x + (60 * xAcc), y - (60 * yAcc), 0);
            obj.transform.localPosition += offset;

            Sprite icon = TradeManager.itemIconDict[item.Name];
            
            foreach (Transform childObj in obj.transform) {
                switch (childObj.gameObject.name)
                {
                    case "Image":
                        childObj.gameObject.GetComponent<Image>().sprite = icon;
                        break;
                    case "BuyPrice":
                        childObj.gameObject.GetComponent<TMP_Text>().text = item.Buy.ToString();
                        break;
                    case "SellPrice":
                        childObj.gameObject.GetComponent<TMP_Text>().text = item.Sell.ToString();
                        break;
                    default:
                        break;
                }
            }

            xAcc += 1;
            if (xAcc == 4)
            {
                yAcc += 1;
                xAcc = 0;
            }
        }
        MoveSelection(0, 0);
    }

    public void MoveSelection(int x, int y)
    {
        // If we attempt to go out of bounds...
        if (currentCursorIDX + x + (4 * (currentCursorIDY + y)) >= traderInventory.Items.Count)
        { return; }

        

        currentCursorIDX = Mathf.Clamp(currentCursorIDX + x, 0, maxItemsPerRow);
        currentCursorIDY = Mathf.Clamp(currentCursorIDY + y, 0, maxItemsPerRow);

        Vector3 newLoc = new Vector3(initX + (itemWidth * currentCursorIDX), initY - (itemHeight * currentCursorIDY), 0);
        currentSelectionOutline.transform.localPosition = newLoc;


        var linearIDX = currentCursorIDX + 4 * currentCursorIDY;
        currentSelectedItem = traderInventory.Items[linearIDX];
    }

    public void BuyItem()
    {
        if (ResourceManager.Coin >= currentSelectedItem.Buy)
        {
            if (currentSelectedItem.Name == "Wood" && ResourceManager.Wood < ResourceManager.woodCap)
            {
                ResourceManager.Wood += 1;
                ResourceManager.Coin -= currentSelectedItem.Buy;
            }
            if (currentSelectedItem.Name == "Wool" && ResourceManager.Wool < ResourceManager.woolCap)
            {
                ResourceManager.Wool += 1; 
                ResourceManager.Coin -= currentSelectedItem.Buy;
            }
        }
    }

    public void SellItem()
    {
        if (currentSelectedItem.Name == "Wood" && ResourceManager.Wood > 0)
        {
            ResourceManager.Wood -= 1;
            ResourceManager.Coin += currentSelectedItem.Sell;
        }
        if (currentSelectedItem.Name == "Wool" && ResourceManager.Wool > 0) {
            ResourceManager.Wool -= 1;
            ResourceManager.Coin += currentSelectedItem.Sell;
        }
    }
}
