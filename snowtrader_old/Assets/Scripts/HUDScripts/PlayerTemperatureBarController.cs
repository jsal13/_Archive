using UnityEngine;
using UnityEngine.UI;

public class PlayerTemperatureBarController : MonoBehaviour
{
    public Slider playerTemperatureSlider;

    private void Awake()
    {
        playerTemperatureSlider = GameObject.Find(DBHierarchyAddr.HUDPlayerTempBar).GetComponent<Slider>();
    }

    private void OnEnable()
    {
        PlayerTemperature.OnCurrentPlayerTemperatureChange += HandlePlayerTemperatureChange;
    }

    private void OnDisable()
    {
        PlayerTemperature.OnCurrentPlayerTemperatureChange -= HandlePlayerTemperatureChange;
    }

    public void HandlePlayerTemperatureChange(float newTemp)
    {
        playerTemperatureSlider.value = newTemp;
    }

}
