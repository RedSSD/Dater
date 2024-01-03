import css from './InvitationPage.module.css'
import MovingButton from "../UI/MovingButton";
import {useState} from "react";
import Button from "../UI/Button";
import {useParams} from "react-router-dom";


const INVITATION_GIF_LINK = "https://media.giphy.com/media/Js27mGWPIUs9V0mjcd/giphy.gif"
const RESULT_GIF_LINK = "https://media.giphy.com/media/j594eyQTt0CiRi9zI5/giphy.gif"
const SUCCESS_TEXT = "YEAAAAHHHHH"

function InvitationPage()
{

    const [gifLink, setGifLink] = useState(INVITATION_GIF_LINK);
    const [text, setText] = useState("Do you wanna go out with me?");

    const urlParams = useParams();

    const checkIsTokenValid = () => {
        // TODO send request and get tg_id or "idi nahui zaebal"
    }

    const OnYesButtonClick = () => {
        setGifLink(RESULT_GIF_LINK);
        setText(SUCCESS_TEXT);
    }

    return (
        <div className={css['invitation-container']}>
            <div>
                <h1>{text}</h1>
            </div>
            <div className={css['gif-container']}>
                <img
                src= {gifLink}
                alt="Cute animated illustration"/>
            </div>
            <div className={css['buttons-section']}>
                <Button
                    text={"Yes"}
                    onClick={OnYesButtonClick}
                />
                <MovingButton>No</MovingButton>
            </div>
        </div>
    )
}

export default InvitationPage;
