using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(PlayerController))]
public class PlayerMovement : EntityMovement
{
    private Rigidbody2D rb;
    private PlayerController player;

    private readonly float walkSpeed = 5.0f;
    private float lastDirection = 1; // last direction the player was.

    public override void Awake()
    {
        base.Awake();
        rb = GetComponent<Rigidbody2D>();
        player = GameObject.Find(DBHierarchyAddr.player).GetComponent<PlayerController>();
    }

    private void Update()
    {
        if (player.canMove) { Move(); }
        else { rb.velocity = new Vector2(0, Mathf.Min(0, rb.velocity.y)); }
    }

    public override void Move()
    {
        // TODO: Maybe I can do something better here?
        if (direction != 0) { lastDirection = Mathf.Sign(direction); }
        direction = GameManager.gamepad.dpad.ReadValue().x;

        // Only change directions if the last direction and the current direction are different.
        if (Mathf.Sign(direction) == lastDirection) { spriteRenderer.flipX = direction == -1; }
        if (direction != 0) { lastDirection = direction; }

        if (!IsObstructed()) { rb.velocity = new Vector2(direction * walkSpeed, rb.velocity.y); }
    }

    public override bool IsObstructed()
    {
        {
            List<int> locs = new List<int> { -1, 1 }; // top and bottom checking.

            foreach (int loc in locs)
            {
                RaycastHit2D hit = Physics2D.Raycast(
                    transform.position + (new Vector3(0, loc * ((objBoxCollider.size.y / 2) - epsilon), 0)),
                    Mathf.Sign(direction) * Vector2.right,
                    (objBoxCollider.size.x / 2) + (2 * epsilon),
                    groundLayer
                );
                if (hit.collider != null) { return true; }
            }
            return false;
        }

    }
}
