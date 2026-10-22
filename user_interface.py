import streamlit as st
from llm_agent import ConversationAgent
import base64


class UserInterface:
    def __init__(self):
        st.set_page_config(page_title="ODIN")
        st.title("ODIN")
        self.conversation_agent_object = self.get_persistent_conversation_agent()

    def get_persistent_conversation_agent(self):

        if "conversation_agent_object" not in st.session_state:
            st.session_state.conversation_agent_object = ConversationAgent()

        return st.session_state.conversation_agent_object

    @staticmethod
    def display_image(base64_image):
        image_bytes = base64.b64decode(base64_image.split(",", 1)[1])
        st.image(image_bytes, width=150)

    @staticmethod
    def display_message(message):
        with st.chat_message(message["role"]):
            for content in message["content"]:
                if content["type"] == "text":
                    st.markdown(content["text"])
                elif content["type"] == "image_url":
                    UserInterface.display_image(content["image_url"]["url"])

    def show_discussion_history(self):
        for message in self.conversation_agent_object.get_conversation_history():
            self.display_message(message)

    @staticmethod
    @st.fragment
    def display_audio_response_toggle():
        st.checkbox("Réponse audio", key="is_audio_response_enabled")

    def play_audio_response(self, llm_response):
        audio_response = self.conversation_agent_object.synthesize_speech(
            llm_response
        )
        st.audio(audio_response, format="audio/mp3", autoplay=True)

    def run(self):
        with st.sidebar:
            self.display_audio_response_toggle()
        is_audio_response_enabled = st.session_state.is_audio_response_enabled

        user_interaction = st.chat_input(
            "ODIN pour te servir, dis moi ce dont tu as besoin ?",
            accept_file=True,
            accept_audio=True,
            file_type=["jpg", "jpeg", "png"],
        )

        if user_interaction:
            if user_interaction.audio:
                text_interaction = self.conversation_agent_object.transcribe(
                    user_interaction.audio.getvalue()
                )
            else:
                text_interaction = user_interaction.text

            image = (
                user_interaction.files[0].getvalue() if user_interaction.files else None
            )

            llm_response = self.conversation_agent_object.ask_llm(
                text_interaction, image
            )
            self.show_discussion_history()

            if is_audio_response_enabled:
                self.play_audio_response(llm_response)


if __name__ == "__main__":
    user_interface_object = UserInterface()
    user_interface_object.run()
