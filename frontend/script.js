/* =====================================================
   ELEMENTS
===================================================== */

const messageInput =
    document.getElementById("messageInput");


const sendButton =
    document.getElementById("sendButton");


const clearButton =
    document.getElementById("clearButton");


const chatMessages =
    document.getElementById("chatMessages");


const typing =
    document.getElementById("typing");


const suggestions =
    document.querySelectorAll(".suggestion");



/* =====================================================
   ADD MESSAGE
===================================================== */

function addMessage(message, sender) {


    const row =
        document.createElement("div");


    row.classList.add(
        "message-row"
    );


    if (sender === "user") {

        row.classList.add(
            "user-row"
        );

    }

    else {

        row.classList.add(
            "ai-row"
        );

    }



    /* =========================================
       AVATAR
    ========================================== */

    const avatar =
        document.createElement("div");


    avatar.classList.add(
        "avatar"
    );


    if (sender === "user") {

        avatar.classList.add(
            "user-avatar"
        );

        avatar.textContent = "👤";

    }

    else {

        avatar.classList.add(
            "ai-avatar"
        );

        avatar.textContent = "🤖";

    }



    /* =========================================
       MESSAGE WRAPPER
    ========================================== */

    const wrapper =
        document.createElement("div");


    wrapper.classList.add(
        "message-wrapper"
    );



    /* =========================================
       NAME
    ========================================== */

    const name =
        document.createElement("div");


    name.classList.add(
        "message-name"
    );


    name.textContent =
        sender === "user"
            ? "You"
            : "AI Assistant";



    /* =========================================
       MESSAGE
    ========================================== */

    const messageElement =
        document.createElement("div");


    messageElement.classList.add(
        "message"
    );


    if (sender === "user") {

        messageElement.classList.add(
            "user-message"
        );

    }

    else {

        messageElement.classList.add(
            "ai-message"
        );

    }


    messageElement.textContent =
        message;



    /* =========================================
       BUILD MESSAGE
    ========================================== */

    wrapper.appendChild(name);

    wrapper.appendChild(messageElement);


    row.appendChild(avatar);

    row.appendChild(wrapper);


    chatMessages.appendChild(row);



    /* Scroll to latest message */

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}



/* =====================================================
   SEND MESSAGE
===================================================== */

async function sendMessage() {


    const message =
        messageInput.value.trim();


    if (!message) {

        return;

    }



    /* Show user message */

    addMessage(
        message,
        "user"
    );



    /* Clear input */

    messageInput.value = "";



    /* Show typing */

    typing.style.display =
        "flex";


    sendButton.disabled =
        true;



    try {


        /*
         * Since FastAPI serves the frontend,
         * we can simply use /chat.
         */

        const response =
            await fetch(
                "/chat",
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body: JSON.stringify({

                        message:
                            message

                    })

                }

            );



        /* Check server response */

        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );

        }



        /* Convert response to JSON */

        const data =
            await response.json();



        /* Show AI response */

        addMessage(
            data.response,
            "assistant"
        );


    }

    catch (error) {


        console.error(
            "Chat error:",
            error
        );


        addMessage(

            "⚠️ I couldn't connect to the AI server. Please make sure FastAPI is running.",

            "assistant"

        );

    }


    finally {


        /* Hide typing */

        typing.style.display =
            "none";


        /* Enable button */

        sendButton.disabled =
            false;


        /* Focus input */

        messageInput.focus();

    }

}



/* =====================================================
   SEND BUTTON
===================================================== */

sendButton.addEventListener(
    "click",
    sendMessage
);



/* =====================================================
   ENTER KEY
===================================================== */

messageInput.addEventListener(

    "keydown",

    function(event) {


        if (

            event.key === "Enter" &&

            !event.shiftKey

        ) {


            event.preventDefault();


            sendMessage();

        }

    }

);



/* =====================================================
   CLEAR CHAT
===================================================== */

clearButton.addEventListener(
    "click",
    async function () {

        try {

            const response = await fetch(
                "/clear",
                {
                    method: "POST"
                }
            );


            if (!response.ok) {

                throw new Error(
                    "Unable to clear conversation"
                );

            }


            // Clear messages from screen

            chatMessages.innerHTML = "";


            // Add fresh assistant message

            addMessage(
                "Chat cleared! ✨ What would you like to talk about?",
                "assistant"
            );


        } catch (error) {

            console.error(
                "Clear error:",
                error
            );


            addMessage(
                "⚠️ Unable to clear conversation memory.",
                "assistant"
            );

        }

    }
);

        /*
    



/* =====================================================
   QUICK SUGGESTIONS
===================================================== */

suggestions.forEach(

    function(button) {


        button.addEventListener(

            "click",

            function() {


                /*
                 * Get predefined message
                 */

                const message =
                    button.dataset.message;



                /*
                 * Put it into input
                 */

                messageInput.value =
                    message;



                /*
                 * Focus input
                 */

                messageInput.focus();


                /*
                 * Automatically send
                 */

                sendMessage();

            }

        );

    }

);



/* =====================================================
   INITIAL FOCUS
===================================================== */

window.addEventListener(

    "load",

    function() {

        messageInput.focus();

    }

);