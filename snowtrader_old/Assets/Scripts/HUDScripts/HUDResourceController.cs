using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class HUDResourceController : MonoBehaviour
{
    private TMP_Text coinText;
    private TMP_Text coinCapText;
    private TMP_Text woodText;
    private TMP_Text woodCapText;
    private TMP_Text woolText;
    private TMP_Text woolCapText;

    private void Awake()
    {
        coinText = GameObject.Find(DBHierarchyAddr.HUDCoinValue).GetComponent<TMP_Text>();
        coinCapText = GameObject.Find(DBHierarchyAddr.HUDCoinCap).GetComponent<TMP_Text>();
        woodText = GameObject.Find(DBHierarchyAddr.HUDWoodValue).GetComponent<TMP_Text>();
        woodCapText = GameObject.Find(DBHierarchyAddr.HUDWoodCap).GetComponent<TMP_Text>();
        woolText = GameObject.Find(DBHierarchyAddr.HUDWoolValue).GetComponent<TMP_Text>();
        woolCapText = GameObject.Find(DBHierarchyAddr.HUDWoolCap).GetComponent<TMP_Text>();
    }

    private void OnEnable()
    {
        ResourceManager.OnPlayerWoolChange += HandlePlayerWoolChange;
        ResourceManager.OnPlayerWoodChange += HandlePlayerWoodChange;
        ResourceManager.OnPlayerCoinChange += HandlePlayerCoinChange;
    }

    private void OnDisable()
    {
        ResourceManager.OnPlayerWoolChange -= HandlePlayerWoolChange;
        ResourceManager.OnPlayerWoodChange -= HandlePlayerWoodChange;
        ResourceManager.OnPlayerCoinChange -= HandlePlayerCoinChange;
    }

    private void HandlePlayerWoodChange(int value)
    {
        woodText.text = value.ToString().PadLeft(3, ' ');
        woodCapText.text = "/" + ResourceManager.woodCap.ToString().PadLeft(3, ' ');
    }

    private void HandlePlayerCoinChange(int value)
    {
        coinText.text = value.ToString().PadLeft(3, ' ');
        coinCapText.text = "/" + ResourceManager.coinCap.ToString().PadLeft(3, ' ');
    }

    private void HandlePlayerWoolChange(int value)
    {
        woolText.text = value.ToString().PadLeft(3, ' ');
        woolCapText.text = "/" + ResourceManager.woolCap.ToString().PadLeft(3, ' ');
    }

}
