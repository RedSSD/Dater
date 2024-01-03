import css from "./Button.module.css";

function Button(props) {
    return (
        <button className={css['answer-button']} onClick={props.onClick}>{props.text}</button>
    )
}

export default Button;
