using UnityEngine;

public class CameraController : MonoBehaviour
{
    public GameObject playerGO;
    public GameObject currentCameraBound;
    public Camera cam;

    [SerializeField] private float cameraVertExtent;
    [SerializeField] private float cameraHorizExtent;

    [SerializeField] private Vector3 cameraBoundExtent;
    [SerializeField] private Vector3 cameraBoundCenter;
    [SerializeField] private float cameraLeftBound;
    [SerializeField] private float cameraRightBound;
    [SerializeField] private float cameraTopBound;
    [SerializeField] private float cameraBottomBound;

    private void Awake()
    {
        InitalizeNewCameraBound();  // TODO: Make this init to something nice.
    }

    void Update()
    {
        float camX = Mathf.Clamp(playerGO.transform.position.x, cameraLeftBound, cameraRightBound);
        float camY = Mathf.Clamp(playerGO.transform.position.y, cameraBottomBound, cameraTopBound);

        cam.transform.position = new Vector3(camX, camY, cam.transform.position.z);
    }

    private void OnEnable()
    {
        PlayerController.OnPlayerCameraTransition += HandlePlayerCameraTransition;
    }

    private void OnDisable()
    {
        PlayerController.OnPlayerCameraTransition -= HandlePlayerCameraTransition;
    }

    private void InitalizeNewCameraBound()
    {
        cameraVertExtent = cam.orthographicSize;
        cameraHorizExtent = cameraVertExtent * cam.aspect;
        var cameraBoundSpriteRenderer = currentCameraBound.GetComponent<SpriteRenderer>();
        cameraBoundExtent = cameraBoundSpriteRenderer.bounds.extents;
        cameraBoundCenter = cameraBoundSpriteRenderer.transform.position;

        cameraLeftBound = cameraBoundCenter.x - cameraBoundExtent.x + cameraHorizExtent;
        cameraRightBound = cameraBoundCenter.x + cameraBoundExtent.x - cameraHorizExtent;
        cameraBottomBound = cameraBoundCenter.y - cameraBoundExtent.y + cameraVertExtent;
        cameraTopBound = cameraBoundCenter.y + cameraBoundExtent.y - cameraVertExtent;
    }

    private void HandlePlayerCameraTransition(GameObject cameraBound)
    {
        GameObject newCameraBound = cameraBound.GetComponent<CameraTransitionController>().toCameraBound;
        if (newCameraBound.name != currentCameraBound.name)
        {
            currentCameraBound = newCameraBound;
            InitalizeNewCameraBound();
        }
    }

}
