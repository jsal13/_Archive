using UnityEngine;

public class ForestController : MonoBehaviour
{
    public Transform[] transforms;
    public SpriteRenderer[] spriteRenders;

    private void OnEnable()
    {
        PlayerChop.OnPlayerTouchingForest += HandlePlayerTouchingForest;
    }

    private void OnDisable()
    {
        PlayerChop.OnPlayerTouchingForest -= HandlePlayerTouchingForest;
    }

    public void HandlePlayerTouchingForest(bool value)
    {
        //// TODO: We can improve this.
        //transforms = GetComponentsInChildren<Transform>();
        //spriteRenders = GetComponentsInChildren<SpriteRenderer>();

        //int boolSign = value ? 1 : -1;
        //for (int idx = 0; idx < transforms.Length; idx += 1)
        //{
        //    transforms[idx].localScale += new Vector3(0, boolSign * 0.1f, 0);
        //}

        //for (int idx = 0; idx < spriteRenders.Length; idx += 1)
        //{
        //    spriteRenders[idx].color = value ? Color.green : Color.white;
        //}

    }

}
