using UnityEngine;

public class PlayerCraft : MonoBehaviour
{
    [SerializeField] private string currentCraftItem;

    private void Update()
    {
        if (GameManager.gamepad.yButton.wasPressedThisFrame) ActionCraftItem(currentCraftItem);
    }

    private void OnEnable()
    {
        CraftItemSelectionController.OnChangedCurrentCraftItem += HandleChangedCurrentCraftItem;
    }

    private void OnDisable()
    {
        CraftItemSelectionController.OnChangedCurrentCraftItem -= HandleChangedCurrentCraftItem;
    }

    public void HandleChangedCurrentCraftItem(string itemName)
    {
        currentCraftItem = itemName;
    }

    public void ActionCraftItem(string itemName)
    {
        // TODO: YO WHERE THE ERROR CHECKING AT?
        foreach (DBCraftItems.CraftItem craftItem in DBCraftItems.GetCraftItemData())
        {
            if (craftItem.name == itemName)
            {
                if (ResourceManager.Wood >= craftItem.cost)
                {
                    Instantiate(craftItem.objectPrefab, transform.position, Quaternion.identity);
                    ResourceManager.Wood -= craftItem.cost;
                }
                else
                {
                    // TODO: Make a honking noise.
                }
            }
        }
    }

}
