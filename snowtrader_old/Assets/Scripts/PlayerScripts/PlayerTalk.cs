using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class PlayerTalk : MonoBehaviour
{
    private GameObject DialogBoxCanvas;
    private TMP_Text DialogBoxTMPText;
    private TMP_Text DialogSpeakerName;
    private Image DialogBoxSpeakerImageComp;
    private Sprite IoSprite;
    private int currentDialogTextIDX;
    [SerializeField] private List<string> dialogText;
    private List<Collider2D> collisionList;
    private CharacterInformation characterInfo;

    [SerializeField] private bool isTalkingToTrader;
    [SerializeField] private bool _isTalking;
    public bool IsTalking
    {
        get => _isTalking;
        set
        {
            _isTalking = value;
            OnPlayerIsTalking?.Invoke(_isTalking);
            SetDialogBoxActive(_isTalking);
            currentDialogTextIDX = _isTalking ? currentDialogTextIDX : 0;
        }
    }

    public delegate void PlayerIsTalking(bool value);
    public static event PlayerIsTalking OnPlayerIsTalking;

    public delegate void PlayerStartedTrading(bool value, GameObject target);
    public static event PlayerStartedTrading OnPlayerStartedTrading;

    private void Awake()
    {
        DialogBoxCanvas = GameObject.Find(DBHierarchyAddr.dialogBoxCanvas);
        DialogBoxTMPText = GameObject.Find(DBHierarchyAddr.dialogBoxText).GetComponent<TMP_Text>();
        DialogSpeakerName = GameObject.Find(DBHierarchyAddr.dialogBoxSpeakerName).GetComponent<TMP_Text>();
        IoSprite = Resources.Load<Sprite>("Images/Io_Character_Sprite");
        DialogBoxSpeakerImageComp = GameObject.Find(DBHierarchyAddr.dialogBoxSpeakerSprite).GetComponent<Image>();
        collisionList = new List<Collider2D>();
    }

    private void Start()
    {
        IsTalking = false;
    }

    private void Update()
    {
        if (GameManager.gamepad.xButton.wasPressedThisFrame && collisionList.Count > 0 && !IsTalking)
        {
            IsTalking = true;
            isTalkingToTrader = collisionList[0].gameObject.GetComponent<CharacterInformation>().tradeType != null;
            GetDialogText(collisionList[0].gameObject);

            currentDialogTextIDX = 0;
            DisplayDialogText(currentDialogTextIDX);
        }

        else if (IsTalking && GameManager.gamepad.xButton.wasPressedThisFrame)
        {
            Debug.Log($"Is talking to trader: {isTalkingToTrader}");
            currentDialogTextIDX += 1;
            if (currentDialogTextIDX < dialogText.Count)
            {
                DisplayDialogText(currentDialogTextIDX);
            }
            else
            {
                IsTalking = false;
                if (isTalkingToTrader)
                {
                    OnPlayerStartedTrading?.Invoke(true, collisionList[0].gameObject);
                    isTalkingToTrader = false;
                }
            }
        }
    }

    private void OnEnable()
    {
        TradeController.OnPlayerEndedTrading += HandlePlayerEndedTrading;
    }

    private void OnDisable()
    {
        TradeController.OnPlayerEndedTrading -= HandlePlayerEndedTrading;
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        var charInfo = collision.GetComponent<CharacterInformation>();
        if (charInfo != null && charInfo.dialogType != null && !collisionList.Contains(collision))
        {
            collisionList.Add(collision);
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        var charInfo = collision.GetComponent<CharacterInformation>();
        if (charInfo != null && charInfo.dialogType != null)
        {
            collisionList.Remove(collision);
        }
    }

    private void GetDialogText(GameObject targetObj)
    {
        characterInfo = targetObj.GetComponent<CharacterInformation>();
        List<List<string>> dialogTexts = DialogManager.GetDialog(characterInfo.dialogType);
        int randomIDX = Random.Range(0, dialogTexts.Count);
        dialogText = dialogTexts[randomIDX];
    }

    private void DisplayDialogText(int IDX)
    {
        var split = dialogText[IDX].Split('|');
        (string name, string txt) = (split[0], split[1]);
        DialogSpeakerName.text = name;
        DialogBoxTMPText.text = txt;
        DialogBoxSpeakerImageComp.sprite = name == "Io" ? IoSprite : characterInfo.characterImage;
    }

    private void SetDialogBoxActive(bool value)
    {
        if (!value)  // Reset values.
        {
            DialogBoxTMPText.text = "";
            DialogSpeakerName.text = "";
            DialogBoxSpeakerImageComp.sprite = null;
        }

        DialogBoxCanvas.SetActive(value);
    }

    private void HandlePlayerEndedTrading()
    {
        isTalkingToTrader = false;
    }

}
