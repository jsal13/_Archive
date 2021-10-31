using System.Collections;
using UnityEngine;

public class FriendOpossumMovement : EntityMovement
{
    private bool isCurrentlyWalkCycled = false;
    [SerializeField] private float initPause;
    [SerializeField] private float walkingDuration;
    [SerializeField] private float walkSpeed = 1.0f;
    public Vector3 startingPos;
    public Vector3 finalPos;
    public float elapsedTime;


    public override void Awake()
    {
        base.Awake();
    }

    private void Start()
    {
        initPause = 5 * Random.value;
        walkingDuration = Random.Range(1, 3);
        direction = 1;
    }

    private void Update()
    {
        Move();
    }

    public override void Move()
    {
        if (!isCurrentlyWalkCycled) StartCoroutine(nameof(WalkCycle));
    }

    IEnumerator WalkCycle()
    {
        isCurrentlyWalkCycled = true;

        yield return new WaitForSeconds(initPause);

        startingPos = transform.position;
        finalPos = transform.position += direction * (new Vector3(1, 0) * walkSpeed * walkingDuration);
        elapsedTime = 0;

        // Change directions
        direction = -direction;
        spriteRenderer.flipX = direction == 1;

        while (elapsedTime < walkingDuration)
        {
            transform.position = Vector3.Lerp(startingPos, finalPos, (elapsedTime / walkingDuration));
            elapsedTime += Time.deltaTime;
            yield return null;
        }

        isCurrentlyWalkCycled = false;
    }

    public override bool IsObstructed()
    {
        return false;
    }
}
