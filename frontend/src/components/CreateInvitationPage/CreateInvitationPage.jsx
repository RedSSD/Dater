import axios from "axios";
import {useRef, useState} from "react";

import css from "./CreateInvitationPage.module.css"
import button_style from "../UI/Button.module.css"


function CreateInvitationPage(){

    const [isCreated, setIsCreated] = useState(false)
    const [invitationLink, setInvitationLink] = useState("")
    const inputIdRef = useRef(null);

    const onCreateButtonClick = () => {
        const telegram_id = inputIdRef.current.value;

        axios.post(`${process.env.REACT_APP_BASE_API_URL}/create/`,
            {"telegram_id": telegram_id}).then(res => {

            if(res.status === 200) {
                setIsCreated(true);
                const link = `${process.env.REACT_APP_PUBLIC_URL}` + `/${res.data["token"]}`
                setInvitationLink(link)
            }
        }).catch((error) =>{
            if(error.response.status === 409){
                alert("Something went wrong. Try to check entered ID.")
            }
        })
    }

    return (
        <div style={{lineHeight: 50 + "pt"}}>
            {!isCreated ?
                <div>
                    <div className={css["form__group field"]}>
                        <input
                            type="input"
                            className={css["form__field"]}
                            placeholder="Telegram ID"
                            id='telegram_id'
                            ref={inputIdRef}
                            required
                        />
                    </div>
                    <button className={button_style['answer-button']} onClick={onCreateButtonClick}>Create</button>
                </div>
                :
                <div>
                    <h2>Your url is</h2>
                    <a href={invitationLink}>{invitationLink}</a>
                </div>
            }
        </div>
    )
}

export default CreateInvitationPage;
