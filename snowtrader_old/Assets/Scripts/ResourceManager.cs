using UnityEngine;

public class ResourceManager : MonoBehaviour
{
    [SerializeField, Range(0, Mathf.Infinity)] private static int _coin = 10;
    public static int coinCap = 20;
    public static int Coin
    {
        get => _coin;
        set
        {
            _coin = Mathf.Clamp(value, 0, coinCap);
            OnPlayerCoinChange?.Invoke(_coin);
        }
    }

    [SerializeField, Range(0, Mathf.Infinity)] private static int _wood = 6;
    public static int woodCap = 12;
    public static int Wood
    {
        get => _wood;
        set
        {
            _wood = Mathf.Clamp(value, 0, woodCap);
            OnPlayerWoodChange?.Invoke(_wood);
        }
    }

    [SerializeField, Range(0, Mathf.Infinity)] private static int _wool = 0;
    public static int woolCap = 4;
    public static int Wool
    {
        get => _wool;
        set
        {
            _wool = Mathf.Clamp(value, 0, woolCap);
            OnPlayerWoolChange?.Invoke(_wool);
        }
    }

    public delegate void PlayerWoodChange(int value);
    public static event PlayerWoodChange OnPlayerWoodChange;

    public delegate void PlayerCoinChange(int value);
    public static event PlayerCoinChange OnPlayerCoinChange;

    public delegate void PlayerWoolChange(int value);
    public static event PlayerWoolChange OnPlayerWoolChange;

    void Start()
    {
        OnPlayerWoodChange?.Invoke(Wood);
        OnPlayerCoinChange?.Invoke(Coin);
        OnPlayerWoolChange?.Invoke(Wool);
    }
}
