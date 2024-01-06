import {useState} from "react";
import axios from "axios";

import MovingButton from "../UI/MovingButton";
import Button from "../UI/Button";
import css from './InvitationPage.module.css'


const INVITATION_GIF_LINK = "https://media.giphy.com/media/Js27mGWPIUs9V0mjcd/giphy.gif"
const RESULT_GIF_LINK = "https://media.giphy.com/media/j594eyQTt0CiRi9zI5/giphy.gif"
const SUCCESS_TEXT = "YEAAAAHHHHH"

function InvitationPage() {
    const [gifLink, setGifLink] = useState(INVITATION_GIF_LINK);
    const [text, setText] = useState("Do you wanna go out with me?");

    const OnYesButtonClick = () => {
        const token = window.location.pathname
        const url = process.env.REACT_APP_BASE_API_URL + `${token}`


        axios.get(url).then(res =>{
            if(res.status === 200) {
                setGifLink(RESULT_GIF_LINK);
                setText(SUCCESS_TEXT);
            }
        })
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
