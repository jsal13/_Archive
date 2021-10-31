using System.Collections;
using UnityEngine;

[RequireComponent(typeof(Animator))]
public class ObjectBonfireController : MonoBehaviour
{
    private Animator animator;
    public float timeBeforeExistinguishSecs = 5f;
    public float timeBeforeDestroySecs = 2f;


    private void Awake()
    {
        animator = GetComponent<Animator>();
    }

    IEnumerator ExtinguishCoroutine()
    {
        yield return new WaitForSeconds(timeBeforeExistinguishSecs);
        animator.SetBool("isExtinguished", true);
        transform.Find("Bonfire_Radius").gameObject.SetActive(false);

        yield return new WaitForSeconds(timeBeforeDestroySecs);
        Destroy(gameObject);
    }

    void Update()
    {
        StartCoroutine(ExtinguishCoroutine());
    }
}
