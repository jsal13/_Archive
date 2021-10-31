using UnityEngine;
using UnityEngine.UI;

[RequireComponent(typeof(Slider))]
public class ChopWoodProgressController : MonoBehaviour
{
    private Slider woodChopProgressSlider;
    private Image[] woodChopProgressImageComponents;

    private void Awake()
    {
        woodChopProgressSlider = GetComponent<Slider>();
        woodChopProgressImageComponents = GetComponentsInChildren<Image>();
    }

    private void OnEnable()
    {
        PlayerChop.OnWoodChopProgress += HandleWoodChopProgress;
    }

    private void OnDisable()
    {
        PlayerChop.OnWoodChopProgress -= HandleWoodChopProgress;
    }

    private void HandleWoodChopProgress(float value)
    {
        woodChopProgressSlider.value = value;
        foreach (Image imageComponent in woodChopProgressImageComponents)
        {
            // Hide the slider if there is a zero value.
            imageComponent.enabled = value != 0;
        }
    }
}
