using System.Collections;
using UnityEngine;

/*
 * TODO: 
 *  - Checkpoint Manager should be separate.
 *  - Where should camera transitions live?
 * 
*/

public class PlayerController : MonoBehaviour
{
    //[Header("Audio")]
    //AudioSource audioCheckpoint;

    [Header("Player Object Information")]
    protected BoxCollider2D objBoxCollider;
    public ContactFilter2D contactFilter;
    protected LayerMask groundLayer;

    [Header("Player Inventory")]
    public bool hasJumpBoots;

    [Header("Player Status Information")]
    public bool isOnGround;
    public bool canMove;

    private bool _isDead;
    public bool IsDead
    {
        get => _isDead;
        set
        {
            _isDead = value;
            if (_isDead)
            {
                canMove = false;
            }
            else
            {
                canMove = true;
            }
        }
    }

    public Vector3 currentCheckpoint;

    public delegate void PlayerCameraTransition(GameObject cameraBound);
    public static event PlayerCameraTransition OnPlayerCameraTransition;

    public delegate void PlayerNearTrader(bool value);
    public static event PlayerNearTrader OnPlayerNearTrader;

    private void Awake()
    {
        currentCheckpoint = GameObject.Find(DBHierarchyAddr.InitialCheckpoint).transform.position + new Vector3(0, 0.5f);

        // Initialize Collision + Movement information.
        objBoxCollider = GetComponent<BoxCollider2D>();
        groundLayer = 1 << LayerMask.NameToLayer("Ground");

        // Contact filter for platforms.
        // TODO: This really ought to be somewhere else.
        contactFilter.useLayerMask = true;
        contactFilter.SetLayerMask(groundLayer);
        contactFilter.useNormalAngle = true;
        contactFilter.SetNormalAngle(89.995f, 90.005f);

    }

    private void Start()
    {
        IsDead = false;
    }

    private void Update()
    {
        isOnGround = objBoxCollider.IsTouching(contactFilter);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Checkpoint"))
        {
            //audioCheckpoint.PlayOneShot(audioCheckpoint.clip, 0.3f);
            currentCheckpoint = collision.gameObject.transform.position + new Vector3(0, 0.5f);
        }

        if (collision.CompareTag("Trader"))
        {
            OnPlayerNearTrader?.Invoke(true);
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.CompareTag("CameraTransition"))
        {
            OnPlayerCameraTransition?.Invoke(collision.gameObject);
        }

        if (collision.CompareTag("Trader"))
        {
            OnPlayerNearTrader?.Invoke(false);
        }
    }

    private void OnEnable()
    {
        PlayerTemperature.OnPlayerDeath += HandlePlayerDeath;
        PlayerTalk.OnPlayerIsTalking += HandlePlayerIsTalking;
        PlayerTalk.OnPlayerStartedTrading += HandlePlayerStartedTrading;
        TradeController.OnPlayerEndedTrading += HandlePlayerEndedTrading;

    }

    private void OnDisable()
    {
        PlayerTemperature.OnPlayerDeath -= HandlePlayerDeath;
        PlayerTalk.OnPlayerIsTalking -= HandlePlayerIsTalking;
        PlayerTalk.OnPlayerStartedTrading -= HandlePlayerStartedTrading;
        TradeController.OnPlayerEndedTrading -= HandlePlayerEndedTrading;
    }

    public void HandlePlayerIsTalking(bool value)
    {
        canMove = !value;
    }

    // TODO: Should combine these two: started and ending trading.
    public void HandlePlayerStartedTrading(bool value, GameObject target)
    {
        canMove = !value;
    }

    public void HandlePlayerEndedTrading()
    {
        canMove = true;
    }

    public void HandlePlayerDeath()
    {
        StartCoroutine(DeathCoroutine());
    }

    IEnumerator DeathCoroutine()
    {
        IsDead = true;
        yield return new WaitForSeconds(1.5f);
        transform.position = currentCheckpoint;
        IsDead = false;
    }

}
