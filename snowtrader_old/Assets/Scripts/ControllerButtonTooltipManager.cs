using UnityEngine;

[RequireComponent(typeof(SpriteRenderer))]
public class ControllerButtonTooltipManager : MonoBehaviour
{
    private SpriteRenderer spriteRenderer;
    //private Sprite buttonA;
    //private Sprite buttonB;
    private Sprite buttonX;
    //private Sprite buttonY;


    private void Awake()
    {
        spriteRenderer = GetComponent<SpriteRenderer>();
        //buttonA = Resources.Load<Sprite>("Images/Buttons_a");
        //buttonB = Resources.Load<Sprite>("Images/Buttons_b");
        buttonX = Resources.Load<Sprite>("Images/Buttons_x");
        //buttonY = Resources.Load<Sprite>("Images/Buttons_y");
    }

    private void OnEnable()
    {
        PlayerChop.OnPlayerTouchingForest += HandlePlayerTouchingForest;
        PlayerController.OnPlayerNearTrader += HandlePlayerNearTrader;
    }

    private void OnDisable()
    {
        PlayerChop.OnPlayerTouchingForest -= HandlePlayerTouchingForest;
        PlayerController.OnPlayerNearTrader -= HandlePlayerNearTrader;
    }

    private void HandlePlayerTouchingForest(bool value)
    {
        if (value)
        {
            spriteRenderer.sprite = buttonX;
        }
        else
        {
            spriteRenderer.sprite = null;
        }
    }

    private void HandlePlayerNearTrader(bool value)
    {
        if (value)
        {
            spriteRenderer.sprite = buttonX;
        }
        else
        {
            spriteRenderer.sprite = null;
        }
    }

}
