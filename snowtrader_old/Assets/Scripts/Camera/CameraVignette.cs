using UnityEngine;

[ExecuteInEditMode]
public class CameraVignette : MonoBehaviour
{
    public Material material;
    public bool isWarm;  // used to cut off vignette if player >= 60 degrees.
    private readonly float initialVRadius = 1.0f;
    private readonly float initialVSoft = 0.6f;
    private float _currentVRadius;
    public float CurrentVRadius
    {
        get => _currentVRadius;
        set
        {
            _currentVRadius = value;
            material.SetFloat("_VRadius", _currentVRadius);
        }
    }

    private float _currentVSoft;
    public float CurrentVSoft
    {
        get => _currentVSoft;
        set
        {
            _currentVSoft = value;
            material.SetFloat("_VSoft", _currentVSoft);
        }
    }

    void OnRenderImage(RenderTexture source, RenderTexture destination)
    {
        Graphics.Blit(source, destination, material);
        CurrentVRadius = 1.0f;
        CurrentVSoft = 0.6f;
    }

    private void OnEnable()
    {
        PlayerTemperature.OnCurrentPlayerTemperatureChange += HandlePlayerTemperatureChange;
    }

    private void OnDisable()
    {
        PlayerTemperature.OnCurrentPlayerTemperatureChange -= HandlePlayerTemperatureChange;
    }

    private void HandlePlayerTemperatureChange(float newTemp)
    {

        if (newTemp >= 60 && !isWarm)
        {
            isWarm = true;
            CurrentVRadius = initialVRadius;
            CurrentVSoft = initialVSoft;
        }
        else if (newTemp < 50 && newTemp > 1)
        {
            isWarm = false;

            var tempPercent = 1 - (newTemp / 50f);
            CurrentVRadius = Mathf.Lerp(1.0f, 0.3f, tempPercent);
            CurrentVSoft = Mathf.Lerp(0.6f, 1.0f, tempPercent);
        }
        else if (newTemp <= 1)
        {
            // Player dies here and resets w/ temperature change.
            material.SetFloat("_VRadius", 0);
        }
    }
}
