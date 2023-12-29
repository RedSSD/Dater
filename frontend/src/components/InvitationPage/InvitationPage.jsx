import css from './InvitationPage.module.css'
import MovingButton from "./MovingButton";


function InvitationPage()
{



    return (
        <div className={css['invitation-container']}>
            <div>
                <h1>Do you wanna go out with me?</h1>
            </div>
            <div className={css['gif-container']}>
                <img
                src= "https://media.giphy.com/media/Js27mGWPIUs9V0mjcd/giphy.gif"
                alt="Cute animated illustration"/>
            </div>
            <div className={css['buttons-section']}>
                <button className={css['answer-button']}>Yes</button>
                <MovingButton>No</MovingButton>
            </div>
        </div>
    )
}

export default InvitationPage;
