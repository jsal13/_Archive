using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class CraftItemSelectionController : MonoBehaviour
{
    private int _currentCraftingItemIDX;
    public int CurrentCraftingItemIDX
    {
        get => _currentCraftingItemIDX;
        set
        {
            if (value == DBCraftItems.GetCraftItemData().Count) _currentCraftingItemIDX = 0;
            else if (value == -1) _currentCraftingItemIDX = DBCraftItems.GetCraftItemData().Count - 1;
            else { _currentCraftingItemIDX = value; }
            SetSelectedCraftingItem(_currentCraftingItemIDX);
        }
    }

    public Image ImageComponentOnHUD;
    public TMP_Text CostComponentOnHUD;

    public delegate void ChangedCurrentCraftItem(string itemName);
    public static event ChangedCurrentCraftItem OnChangedCurrentCraftItem;


    private void Awake()
    {
        ImageComponentOnHUD = GameObject.Find(DBHierarchyAddr.SelectedCraftItem).GetComponent<Image>();
        CostComponentOnHUD = GameObject.Find(DBHierarchyAddr.SelectedCraftItemCost).GetComponent<TMP_Text>(); ;
    }

    private void Start()
    {
        SetSelectedCraftingItem(0);
    }

    private void OnEnable()
    {
        ResourceManager.OnPlayerWoodChange += HandlePlayerWoodChange;
    }

    private void OnDisable()
    {
        ResourceManager.OnPlayerWoodChange -= HandlePlayerWoodChange;
    }

    void Update()
    {
        // Only update the sprite if there's an update to the IDX.
        if (GameManager.gamepad.leftShoulder.wasPressedThisFrame) CurrentCraftingItemIDX -= 1;
        else if (GameManager.gamepad.rightShoulder.wasPressedThisFrame) CurrentCraftingItemIDX += 1;
    }

    public void SetSelectedCraftingItem(int idx)
    {
        OnChangedCurrentCraftItem?.Invoke(DBCraftItems.GetCraftItemData()[idx].name);
        ImageComponentOnHUD.sprite = DBCraftItems.GetCraftItemData()[idx].sprite;
        CostComponentOnHUD.text = DBCraftItems.GetCraftItemData()[idx].cost.ToString();

        if (ResourceManager.Wood < DBCraftItems.GetCraftItemData()[idx].cost)
        {
            ImageComponentOnHUD.color = Color.red;
            CostComponentOnHUD.color = Color.red;
        }
        else
        {
            ImageComponentOnHUD.color = Color.white;
            CostComponentOnHUD.color = Color.black;
        }

    }

    public void HandlePlayerWoodChange(int value)
    {
        // Checks to see if we can afford things now.
        SetSelectedCraftingItem(CurrentCraftingItemIDX);
    }

}
