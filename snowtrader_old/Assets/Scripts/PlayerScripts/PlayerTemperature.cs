using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerTemperature : MonoBehaviour
{
    PlayerController player;
    bool canChangeTemperature = true;
    [SerializeField] List<Collider2D> temperatureColliders = new List<Collider2D>();
    private readonly float initAmbientTemperature = -2f;
    [SerializeField] private float playerTemperatureChangePerSecond = 0;
    [SerializeField, Range(0, 100)] private float _currentPlayerTemperature = 80.0f;
    public float CurrentPlayerTemperature
    {
        get => _currentPlayerTemperature;
        set
        {
            if (!canChangeTemperature) return;
            else
            {
                _currentPlayerTemperature = Mathf.Clamp(value, 0, 100);
                OnCurrentPlayerTemperatureChange?.Invoke(value);
            }
        }
    }

    public delegate void CurrentPlayerTemperatureChange(float newTemp);
    public static event CurrentPlayerTemperatureChange OnCurrentPlayerTemperatureChange;

    public delegate void PlayerDeath();
    public static event PlayerDeath OnPlayerDeath;

    private void Awake()
    {
        player = GetComponent<PlayerController>(); // TODO: only need this for "isDead".    
    }

    private void Start()
    {
        OnCurrentPlayerTemperatureChange?.Invoke(CurrentPlayerTemperature);
    }

    private void OnEnable()
    {
        OnPlayerDeath += HandlePlayerDeath;
        PlayerTalk.OnPlayerIsTalking += HandlePlayerIsTalking;
        PlayerTalk.OnPlayerStartedTrading += HandlePlayerStartedTrading;
        TradeController.OnPlayerEndedTrading += HandlePlayerEndedTrading;
    }

    private void OnDisable()
    {
        OnPlayerDeath -= HandlePlayerDeath;
        PlayerTalk.OnPlayerIsTalking -= HandlePlayerIsTalking;
        PlayerTalk.OnPlayerStartedTrading -= HandlePlayerStartedTrading;
        TradeController.OnPlayerEndedTrading -= HandlePlayerEndedTrading;
    }

    void OnTriggerEnter2D(Collider2D collision)
    {
        // TODO: Can we do get;set; with the temp collider list?
        if (!temperatureColliders.Contains(collision) && collision.CompareTag("Temperature"))
        {
            temperatureColliders.Add(collision);
            RecalculateTemperature();
        };
    }
    void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.CompareTag("Temperature"))
        {
            temperatureColliders.Remove(collision);
            RecalculateTemperature();
        }

    }

    private void RecalculateTemperature()
    {
        // Add up the current colliders value, or set the value to zero if there are none.
        if (temperatureColliders.Count > 0)
        {
            foreach (Collider2D col in temperatureColliders)
            {
                playerTemperatureChangePerSecond = col.GetComponent<TemperatureController>().temperature;
            }
        }
        else
        {
            playerTemperatureChangePerSecond = 0;
        }

        // Add on ambient temperature of area.
        playerTemperatureChangePerSecond += initAmbientTemperature;
    }

    private void Update()
    {
        CurrentPlayerTemperature += Mathf.Clamp(playerTemperatureChangePerSecond, -10, 10) * Time.deltaTime;
        if (CurrentPlayerTemperature <= 0 & !player.IsDead) OnPlayerDeath();
    }

    public void HandlePlayerDeath()
    {
        StartCoroutine(DeathCoroutine());
    }

    IEnumerator DeathCoroutine()
    {
        yield return new WaitForSeconds(1.5f);
        CurrentPlayerTemperature = 90.0f;
    }

    public void HandlePlayerIsTalking(bool value)
    {
        canChangeTemperature = !value;
    }

    // TODO: Put these two together.
    private void HandlePlayerStartedTrading(bool value, GameObject target)
    {
        canChangeTemperature = !value;
    }

    private void HandlePlayerEndedTrading()
    {
        canChangeTemperature = true;
    }

}
