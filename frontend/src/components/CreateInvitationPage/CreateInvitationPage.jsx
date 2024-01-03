import css from "./CreateInvitationPage.module.css"
import Button from "../UI/Button";

function CreateInvitationPage(){

    const onCreateButtonClick = () => {

    }

    return (
        <div style={{lineHeight: 50 + "pt"}}>
            <div className={css["form__group field"]}>
                <input type="input" className={css["form__field"]} placeholder="Telegram ID" name="TH" id='name'
                       required/>
            </div>
            <Button
                text="Create"
                onCLick={onCreateButtonClick}
            />
        </div>

    )
}

export default CreateInvitationPage;
