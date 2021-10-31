using UnityEngine;

[RequireComponent(typeof(SpriteRenderer))]
[RequireComponent(typeof(BoxCollider2D))]
public abstract class EntityMovement : MonoBehaviour
{
    protected SpriteRenderer spriteRenderer;
    protected BoxCollider2D objBoxCollider;

    protected LayerMask groundLayer;
    protected float direction;
    public float epsilon = 0.05f;

    public virtual void Awake()
    {
        spriteRenderer = GetComponent<SpriteRenderer>();
        objBoxCollider = GetComponent<BoxCollider2D>();
        groundLayer = 1 << LayerMask.NameToLayer("Ground");
    }

    public abstract void Move();
    public abstract bool IsObstructed();
}
