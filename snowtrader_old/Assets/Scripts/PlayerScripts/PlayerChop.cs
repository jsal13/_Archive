using System.Collections;
using UnityEngine;

/* BUGS:
 *[Fixed?] Pressing jump a frame before (possibly at the same time?) as chopping would put the player into an unmovable state.
 */

[RequireComponent(typeof(PlayerController))]
public class PlayerChop : MonoBehaviour
{
    public GameManager gameManager;
    public PlayerController player;

    public bool canChopTrees = false;
    private readonly float chopTreesDuration = 2f;
    private Coroutine woodChopCoroutine;
    private float woodChopStartTime;
    [SerializeField] private float _woodChopProgressPercent;
    public float WoodChopProgressPercent
    {
        get => _woodChopProgressPercent;
        set
        {
            // If it reaches 100%, reset it to 0.
            if (value < 1) _woodChopProgressPercent = value;
            else _woodChopProgressPercent = 0;

            OnWoodChopProgress(_woodChopProgressPercent);
        }
    }

    public delegate void PlayerTouchingForest(bool value);
    public static event PlayerTouchingForest OnPlayerTouchingForest;

    public delegate void WoodChopProgress(float value);
    public static event WoodChopProgress OnWoodChopProgress;

    public void Awake()
    {
        player = GetComponent<PlayerController>();
    }

    public void Start()
    {
        OnWoodChopProgress?.Invoke(0);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Trees"))
        {
            OnPlayerTouchingForest?.Invoke(true);
        }
    }

    private void OnTriggerStay2D(Collider2D collision)
    {
        if (collision.CompareTag("Trees"))
        {
            if (player.canMove && player.isOnGround && WoodChopProgressPercent == 0) canChopTrees = true;
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.CompareTag("Trees"))
        {
            canChopTrees = false;
            WoodChopProgressPercent = 0;
            OnPlayerTouchingForest?.Invoke(false);
        }
    }

    private void Update()
    {
        if ((GameManager.gamepad.xButton.isPressed && canChopTrees) || WoodChopProgressPercent > 0) ActionChopTrees();
    }

    public void ActionChopTrees()
    {
        if (canChopTrees && WoodChopProgressPercent == 0)
        {
            player.canMove = false;
            WoodChopProgressPercent = 0.001f;
            woodChopStartTime = Time.time;
            woodChopCoroutine = StartCoroutine(ChopTrees());
        }
        else if (GameManager.gamepad.xButton.isPressed && WoodChopProgressPercent > 0)
        {
            WoodChopProgressPercent = (Time.time - woodChopStartTime) / chopTreesDuration;
        }

        else if (GameManager.gamepad.xButton.wasReleasedThisFrame)
        {
            StopCoroutine(woodChopCoroutine);
            WoodChopProgressPercent = 0;
            player.canMove = true;
        }
    }

    public IEnumerator ChopTrees()
    {
        yield return new WaitForSeconds(chopTreesDuration);
        ResourceManager.Wood += 1;
    }
}
