using UnityEngine;

[RequireComponent(typeof(Rigidbody2D))]
public abstract class EntityJump : MonoBehaviour
{
    protected Rigidbody2D rb;
    protected float fallMaxVelocity = 14.0f;
    protected float xVel;
    protected float yVel;

    public virtual void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    public abstract void Jump();
}