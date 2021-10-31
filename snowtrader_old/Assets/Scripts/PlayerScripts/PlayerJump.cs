using UnityEngine;

[RequireComponent(typeof(PlayerController))]
public class PlayerJump : EntityJump
{
    private PlayerController player;
    private readonly float jumpForce = 600f;
    private readonly float jumpMinVelocity = 1f;
    private int jumpCount = 0;
    private int jumpCountMax = 1;

    public override void Awake()
    {
        base.Awake();
        player = GetComponent<PlayerController>();
    }

    private void Update()
    {
        Jump();
    }

    private void FixedUpdate()
    {
        // Clamped max fall velocity.
        if (rb.velocity.y < -Mathf.Abs(fallMaxVelocity))
        {
            rb.velocity = new Vector2(
                rb.velocity.x,
                Mathf.Clamp(rb.velocity.y, -Mathf.Abs(fallMaxVelocity), Mathf.Infinity)
            );
        }
    }

    public bool PlayerPressedJump() { return GameManager.gamepad.aButton.wasPressedThisFrame; }
    public bool PlayerReleasedJump() { return GameManager.gamepad.aButton.wasReleasedThisFrame; }

    public override void Jump()
    {
        
        if (player.isOnGround && player.canMove && PlayerPressedJump()) // Normal Jump (at full speed)
        {
            rb.velocity = new Vector2(rb.velocity.x, 0); // 0 out the y velocity.
            rb.AddForce(new Vector2(0, jumpForce));
            jumpCount = 1;
        }
        else if (PlayerPressedJump() && player.canMove && jumpCount < jumpCountMax)
        {
            rb.velocity = new Vector2(rb.velocity.x, 0); // 0 out the y velocity.
            rb.AddForce(new Vector2(0, 0.8f * jumpForce));
            jumpCount += 1;
        }

        if (PlayerReleasedJump()) // Shortened jump (small taps)
        {
            rb.velocity = new Vector2(rb.velocity.x, Mathf.Min(rb.velocity.y, jumpMinVelocity)); 
        }
    }
}
