import css from './InvitationPage.module.css'
import MovingButton from "./MovingButton";
import {useState} from "react";


const INVITATION_GIF_LINK = "https://media.giphy.com/media/Js27mGWPIUs9V0mjcd/giphy.gif"
const RESULT_GIF_LINK = "https://media.giphy.com/media/j594eyQTt0CiRi9zI5/giphy.gif"

function InvitationPage()
{

    const [gifLink, setGifLink] = useState(INVITATION_GIF_LINK);
    const [text, setText] = useState("Do you wanna go out with me?");

    const OnYesButtonClick = () => {
        setGifLink(RESULT_GIF_LINK);
        setText("YEAAAAHHHHH");
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
                <button className={css['answer-button']} onClick={OnYesButtonClick}>Yes</button>
                <MovingButton>No</MovingButton>
            </div>
        </div>
    )
}

export default InvitationPage;
