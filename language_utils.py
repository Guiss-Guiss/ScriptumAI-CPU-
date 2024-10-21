import streamlit as st

translations = {
    'en': {
        'title': "ScriptumAI",
        'navigation': "Navigation",
        'upload': "Upload",
        'search': "Search",
        'manage_documents': "Manage Documents",
        'settings': "Settings",
        'save': "Save",
        'delete': "Delete",
        'edit': "Edit",
        'update': "Update",
        'cancel': "Cancel",
        'back': "Back",
        'next': "Next",
        'finish': "Finish",
        'loading': "Loading...",
        'processing': "Processing...",
        'success': "Success!",
        'error': "Error",
        'warning': "Warning",
        'info': "Information",
        'document_upload': "Document Upload",
        'choose_files': "Choose files",
        'processing_files': "Processing files and generating embeddings...",
        'files_processed': "All files processed and embeddings generated successfully!",
        'file_processed_success': "File '{file_name}' processed and embedded successfully!",
        'embedding_generation_failed': "Failed to generate embeddings for {file_name}.",
        'file_processing_failed': "Failed to process {file_name}.",
        'file_processing_error': "Error processing file {file_name}: {error}",
        'embedding_error': "Error: {0}",
        'processing_status': "Processing: {file_name} ({processed}/{total})",
        'processing_complete': "All files processed successfully!",
        'search_qa': "Document Search and Question Answering",
        'enter_query': "Enter your query or question:",
        'num_results': "Number of results",
        'confidence_threshold': "Confidence threshold",
        'search_answer': "Search and Answer",
        'searching': "Searching and generating answer...",
        'generated_answer': "Generated Answer:",
        'relevant_chunks': "Relevant Document Chunks:",
        'no_relevant_docs': "No relevant documents found for the given query and confidence threshold.",
        'chunk_content': "Content:",
        'chunk_similarity': "Similarity Score:",
        'chunk_metadata': "Metadata:",
        'document_management': "Document Management",
        'uploaded_files': "Uploaded Files:",
        'file_deleted': "File {file_name} and all its associated data deleted successfully",
        'delete_failed': "Failed to delete file {file_name}: {error}",
        'no_files_found': "No files found in the database.",
        'delete_note': "Note: Deleting a file removes all associated documents and their embeddings from the database. This action cannot be undone.",
        'confirm_delete': "Are you sure you want to delete this file?",
        'user_preferences': "User Preferences",
        'language_selection': "Language / Idioma / Langue",
        'save_preferences': "Save Preferences",
        'preferences_saved': "Preferences saved successfully!",
        'default_number_of_results': "Default number of results",
        'default_confidence_threshold': "Default confidence threshold",
        'unexpected_error': "An unexpected error occurred: {0}",
        'component_init_error': "Failed to initialize components: {0}",
        'query_processing_error': "Error processing query: {0}",
        'app_runtime_error': "Failed to run the application: {error}",
        'yes': "Yes",
        'no': "No",
        'ok': "OK",
        'apply': "Apply",
        'reset': "Reset",
        'learn_more': "Learn More",
        'help': "Help",
        'about': "About",
        'version': "Version",
        'go_to': "Go to",
        'answer_language_note': "Note: The answer is generated in the question's language.",
        "processing_file": "Processing file: {file_name}",
        "failed_to_process": "Failed to process {file_name}",
        "text_chunked": "Text chunked into {chunk_count} chunks",
        "embeddings_generated": "Embeddings generated successfully for {file_name}",
        "no_embeddings_generated": "No embeddings generated for {file_name}",
        "error_processing_file": "Error processing file {file_name}: {error}",
        "saved_processed_content": "Saved processed content to {file_path}",
        "error_occurred": "An error occurred: {error}",
        "error_listing_files": "Error listing files: {error}",
        "file_deleted_success": "File {file_name} and all its associated documents and embeddings deleted successfully",
        "error_deleting_file": "Error deleting file {file_name}: {error}",
        "failed_to_list_files": "Failed to list files: {error}",
        "error_in_document_management": "Error in render_document_management: {error}",
        "rag_component_initialized": "RAGComponent initialized with model: {model}",
        "generating_answer_for_query": "Generating answer for query: {query}",
        "answer_generated_successfully": "Answer generated successfully",
        "no_valid_response_from_model": "No valid response from the model",
        "couldnt_generate_answer": "I'm sorry, I couldn't generate an answer at this time.",
        "error_generating_answer": "Error generating answer: {error}",
        "error_occurred_while_generating": "An error occurred while generating the answer: {error}",
        "rag_prompt": """
            You are an AI assistant specialized in the literary analysis. Your task is to provide detailed and in-depth answers based on the given context. Follow these guidelines:

                1. Carefully analyze all the provided excerpts.
                2. Synthesize the information from multiple excerpts to form a coherent and detailed answer.
                3. If the context contains information about specific characters, events, or concepts, elaborate on them.
                4. Provide examples or explanations to support your points whenever possible.
                5. If there are multiple perspectives or interpretations in the excerpts, discuss them.
                6. If the excerpts do not contain enough information to fully answer the question, clearly indicate what is known and what remains uncertain.
                7. Organize your response logically, using paragraphs to separate different points or aspects of the answer.
                8. Aim for an answer of at least 150 words, but expand further if the information and question justify it.

                Base your response primarily on the provided context. If you make inferences or connections beyond the given information, clearly state it.
                If the query language is not English, please provide the response in the detected language.

            Context:
            {context}

            User Question: {query}

            Assistant:
            """,
        "retrieval_system_initialized": "RetrievalSystem initialized",
        "fetching_relevant_chunks": "Fetching relevant chunks for query: {query}",
        "retrieved_relevant_chunks": "Retrieved {chunk_count} relevant chunks after filtering by confidence threshold: {confidence_threshold}",
        "error_fetching_chunks": "Error fetching relevant chunks: {error}",
        'refresh_to_apply': "Refresh the page to apply changes",
    },
    'es': {
        'title': "ScriptumAI",
        'navigation': "Navegación",
        'upload': "Subir",
        'search': "Buscar",
        'manage_documents': "Gestionar Documentos",
        'settings': "Configuración",
        'save': "Guardar",
        'delete': "Eliminar",
        'edit': "Editar",
        'update': "Actualizar",
        'cancel': "Cancelar",
        'back': "Atrás",
        'next': "Siguiente",
        'finish': "Finalizar",
        'loading': "Cargando...",
        'processing': "Procesando...",
        'success': "¡Éxito!",
        'error': "Error",
        'warning': "Advertencia",
        'info': "Información",
        'document_upload': "Subir Documento",
        'choose_files': "Elegir archivos",
        'processing_files': "Procesando archivos y generando embeddings...",
        'files_processed': "Todos los archivos procesados y embeddings generados con éxito!",
        'file_processed_success': "¡Archivo '{file_name}' procesado e incrustado con éxito!",
        'embedding_generation_failed': "Error al generar incrustaciones para {file_name}.",
        'file_processing_failed': "Error al procesar {file_name}.",
        'file_processing_error': "Error al procesar el archivo {file_name}: {error}",
        'embedding_error': "Error: {0}",
        'processing_status': "Procesando: {file_name} ({processed}/{total})",
        'processing_complete': "¡Todos los archivos procesados con éxito!",
        'search_qa': "Búsqueda de Documentos y Respuesta a Preguntas",
        'enter_query': "Ingrese su consulta o pregunta:",
        'num_results': "Número de resultados",
        'confidence_threshold': "Umbral de confianza",
        'search_answer': "Buscar y Responder",
        'searching': "Buscando y generando respuesta...",
        'generated_answer': "Respuesta Generada:",
        'relevant_chunks': "Fragmentos de Documentos Relevantes:",
        'no_relevant_docs': "No se encontraron documentos relevantes para la consulta y el umbral de confianza dados.",
        'chunk_content': "Contenido:",
        'chunk_similarity': "Puntuación de Similitud:",
        'chunk_metadata': "Metadatos:",
        'document_management': "Gestión de Documentos",
        'uploaded_files': "Archivos Subidos:",
        'file_deleted': "Archivo {file_name} y todos sus datos asociados eliminados con éxito",
        'delete_failed': "Error al eliminar el archivo {file_name}: {error}",
        'no_files_found': "No se encontraron archivos en la base de datos.",
        'delete_note': "Nota: Eliminar un archivo elimina todos los documentos asociados y sus embeddings de la base de datos. Esta acción no se puede deshacer.",
        'confirm_delete': "¿Está seguro de que desea eliminar este archivo?",
        'user_preferences': "Preferencias de Usuario",
        'language_selection': "Language / Idioma / Langue",
        'save_preferences': "Guardar Preferencias",
        'preferences_saved': "¡Preferencias guardadas con éxito!",
        'default_number_of_results': "Número predeterminado de resultados",
        'default_confidence_threshold': "Umbral de confianza predeterminado",
        'unexpected_error': "Ocurrió un error inesperado: {0}",
        'component_init_error': "Error al inicializar los componentes: {0}",
        'query_processing_error': "Error al procesar la consulta: {0}",
        'app_runtime_error': "Error al ejecutar la aplicación: {error}",
        'yes': "Sí",
        'no': "No",
        'ok': "OK",
        'apply': "Aplicar",
        'reset': "Restablecer",
        'learn_more': "Más Información",
        'help': "Ayuda",
        'about': "Acerca de",
        'version': "Versión",
        'go_to': "Ir a",
        'answer_language_note': "Nota: La respuesta se genera en el idioma de la pregunta.",
           "processing_file": "Procesando archivo: {file_name}",
        "failed_to_process": "Error al procesar {file_name}",
        "text_chunked": "Texto dividido en {chunk_count} fragmentos",
        "embeddings_generated": "Embeddings generados con éxito para {file_name}",
        "no_embeddings_generated": "No se generaron embeddings para {file_name}",
        "error_processing_file": "Error al procesar el archivo {file_name}: {error}",
        "saved_processed_content": "Contenido procesado guardado en {file_path}",
        "error_occurred": "Ocurrió un error: {error}",
        "error_listing_files": "Error al listar archivos: {error}",
        "file_deleted_success": "Archivo {file_name} y todos sus documentos y embeddings asociados eliminados con éxito",
        "error_deleting_file": "Error al eliminar el archivo {file_name}: {error}",
        "failed_to_list_files": "Error al listar archivos: {error}",
        "error_in_document_management": "Error en render_document_management: {error}",
        "rag_component_initialized": "RAGComponent inicializado con el modelo: {model}",
        "generating_answer_for_query": "Generando respuesta para la consulta: {query}",
        "answer_generated_successfully": "Respuesta generada con éxito",
        "no_valid_response_from_model": "No se obtuvo una respuesta válida del modelo",
        "couldnt_generate_answer": "Lo siento, no pude generar una respuesta en este momento.",
        "error_generating_answer": "Error al generar la respuesta: {error}",
        "error_occurred_while_generating": "Ocurrió un error al generar la respuesta: {error}",
        "rag_prompt": """
            Eres un asistente de IA especializado en análisis literario. Tu tarea es proporcionar respuestas detalladas y profundas basadas en el contexto dado. Sigue estas pautas:

                1. Analiza cuidadosamente todos los extractos proporcionados.
                2. Sintetiza la información de múltiples extractos para formar una respuesta coherente y detallada.
                3. Si el contexto contiene información sobre personajes, eventos o conceptos específicos, elabora sobre ellos.
                4. Proporciona ejemplos o explicaciones para respaldar tus puntos siempre que sea posible.
                5. Si hay múltiples perspectivas o interpretaciones en los extractos, discútelas.
                6. Si los extractos no contienen suficiente información para responder completamente a la pregunta, indica claramente lo que se sabe y lo que queda incierto.
                7. Organiza tu respuesta de manera lógica, utilizando párrafos para separar diferentes puntos o aspectos de la respuesta.
                8. Apunta a una respuesta de al menos 150 palabras, pero amplía más si la información y la pregunta lo justifican.

                Basa tu respuesta principalmente en el contexto proporcionado. Si haces inferencias o conexiones más allá de la información dada, indícalo claramente.
                Si el idioma de la consulta no es español, proporciona la respuesta en el idioma detectado.

            Contexto:
            {context}

            Pregunta del Usuario: {query}

            Asistente:
            """,
        "retrieval_system_initialized": "Sistema de recuperación inicializado",
        "fetching_relevant_chunks": "Buscando fragmentos relevantes para la consulta: {query}",
        "retrieved_relevant_chunks": "Se recuperaron {chunk_count} fragmentos relevantes después de filtrar por umbral de confianza: {confidence_threshold}",
        "error_fetching_chunks": "Error al obtener fragmentos relevantes: {error}",
        'refresh_to_apply': "Actualice la página para aplicar los cambios",
    },
    'fr': {
        'title': "ScriptumAI",
        'navigation': "Navigation",
        'upload': "Télécharger",
        'search': "Rechercher",
        'manage_documents': "Gérer les Documents",
        'settings': "Paramètres",
        'save': "Enregistrer",
        'delete': "Supprimer",
        'edit': "Modifier",
        'update': "Mettre à jour",
        'cancel': "Annuler",
        'back': "Retour",
        'next': "Suivant",
        'finish': "Terminer",
        'loading': "Chargement...",
        'processing': "Traitement...",
        'success': "Succès !",
        'error': "Erreur",
        'warning': "Avertissement",
        'info': "Information",
        'document_upload': "Téléchargement de Document",
        'choose_files': "Choisir les fichiers",
        'processing_files': "Traitement des fichiers et génération des embeddings...",
        'files_processed': "Tous les fichiers traités et embeddings générés avec succès !",
        'file_processed_success': "Fichier '{file_name}' traité et intégré avec succès !",
        'embedding_generation_failed': "Échec de la génération des intégrations pour {file_name}.",
        'file_processing_failed': "Échec du traitement de {file_name}.",
        'file_processing_error': "Erreur lors du traitement du fichier {file_name} : {error}",
        'embedding_error': "Erreur : {0}",
        'processing_status': "Traitement : {file_name} ({processed}/{total})",
        'processing_complete': "Tous les fichiers ont été traités avec succès !",
        'search_qa': "Recherche de Documents et Réponse aux Questions",
        'enter_query': "Entrez votre requête ou question :",
        'num_results': "Nombre de résultats",
        'confidence_threshold': "Seuil de confiance",
        'search_answer': "Rechercher et Répondre",
        'searching': "Recherche et génération de réponse en cours...",
        'generated_answer': "Réponse Générée :",
        'relevant_chunks': "Fragments de Documents Pertinents :",
        'no_relevant_docs': "Aucun document pertinent trouvé pour la requête et le seuil de confiance donnés.",
        'chunk_content': "Contenu :",
        'chunk_similarity': "Score de Similarité :",
        'chunk_metadata': "Métadonnées :",
        'document_management': "Gestion des Documents",
        'uploaded_files': "Fichiers Téléchargés :",
        'file_deleted': "Fichier {file_name} et toutes ses données associées supprimés avec succès",
        'delete_failed': "Échec de la suppression du fichier {file_name} : {error}",
        'no_files_found': "Aucun fichier trouvé dans la base de données.",
        'delete_note': "Note : La suppression d'un fichier supprime tous les documents associés et leurs embeddings de la base de données. Cette action ne peut pas être annulée.",
        'confirm_delete': "Êtes-vous sûr de vouloir supprimer ce fichier ?",
        'user_preferences': "Préférences Utilisateur",
        'language_selection': "Language / Idioma / Langue",
        'save_preferences': "Enregistrer les Préférences",
        'preferences_saved': "Préférences enregistrées avec succès !",
        'default_number_of_results': "Nombre de résultats par défaut",
        'default_confidence_threshold': "Seuil de confiance par défaut",
        'unexpected_error': "Une erreur inattendue s'est produite : {0}",
        'component_init_error': "Échec de l'initialisation des composants : {0}",
        'query_processing_error': "Erreur lors du traitement de la requête : {0}",
        'app_runtime_error': "Échec de l'exécution de l'application : {error}",
        'yes': "Oui",
        'no': "Non",
        'ok': "OK",
        'apply': "Appliquer",
        'reset': "Réinitialiser",
        'learn_more': "En Savoir Plus",
        'help': "Aide",
        'about': "À Propos",
        'version': "Version",
        'go_to': "Aller à",
        'answer_language_note': "Note : La réponse est générée dans la langue de la question.",
        "processing_file": "Traitement du fichier : {file_name}",
        "failed_to_process": "Échec du traitement de {file_name}",
        "text_chunked": "Texte découpé en {chunk_count} fragments",
        "embeddings_generated": "Embeddings générés avec succès pour {file_name}",
        "no_embeddings_generated": "Aucun embedding généré pour {file_name}",
        "error_processing_file": "Erreur lors du traitement du fichier {file_name} : {error}",
        "saved_processed_content": "Contenu traité sauvegardé dans {file_path}",
        "error_occurred": "Une erreur s'est produite : {error}",
        "error_listing_files": "Erreur lors de la liste des fichiers : {error}",
        "file_deleted_success": "Fichier {file_name} et tous ses documents et embeddings associés supprimés avec succès",
        "error_deleting_file": "Erreur lors de la suppression du fichier {file_name} : {error}",
        "failed_to_list_files": "Échec de la liste des fichiers : {error}",
        "error_in_document_management": "Erreur dans render_document_management : {error}",
        "rag_component_initialized": "RAGComponent initialisé avec le modèle : {model}",
        "generating_answer_for_query": "Génération de la réponse pour la requête : {query}",
        "answer_generated_successfully": "Réponse générée avec succès",
        "no_valid_response_from_model": "Pas de réponse valide du modèle",
        "couldnt_generate_answer": "Désolé, je n'ai pas pu générer une réponse pour le moment.",
        "error_generating_answer": "Erreur lors de la génération de la réponse : {error}",
        "error_occurred_while_generating": "Une erreur s'est produite lors de la génération de la réponse : {error}",
        "rag_prompt": """
            Vous êtes un assistant IA spécialisé dans l'analyse littéraire. Votre tâche est de fournir des réponses détaillées et approfondies basées sur le contexte donné. Suivez ces directives :

                1. Analysez soigneusement tous les extraits fournis.
                2. Synthétisez les informations de plusieurs extraits pour former une réponse cohérente et détaillée.
                3. Si le contexte contient des informations sur des personnages, des événements ou des concepts spécifiques, élaborez à leur sujet.
                4. Fournissez des exemples ou des explications pour étayer vos points chaque fois que possible.
                5. S'il y a plusieurs perspectives ou interprétations dans les extraits, discutez-en.
                6. Si les extraits ne contiennent pas suffisamment d'informations pour répondre pleinement à la question, indiquez clairement ce qui est connu et ce qui reste incertain.
                7. Organisez votre réponse de manière logique, en utilisant des paragraphes pour séparer les différents points ou aspects de la réponse.
                8. Visez une réponse d'au moins 150 mots, mais développez davantage si l'information et la question le justifient.

                Basez votre réponse principalement sur le contexte fourni. Si vous faites des déductions ou des connexions au-delà des informations données, indiquez-le clairement.
                Si la langue de la requête n'est pas le français, veuillez fournir la réponse dans la langue détectée.

            Contexte :
            {context}

            Question de l'utilisateur : {query}

            Assistant :
            """,
        "retrieval_system_initialized": "Système de récupération initialisé",
        "fetching_relevant_chunks": "Récupération des fragments pertinents pour la requête : {query}",
        "retrieved_relevant_chunks": "Récupéré {chunk_count} fragments pertinents après filtrage par seuil de confiance : {confidence_threshold}",
        "error_fetching_chunks": "Erreur lors de la récupération des fragments pertinents : {error}",
        'refresh_to_apply': "Rafraîchir la page pour appliquer les modifications",
},
     
    }


def get_translation(key, lang=None, **kwargs):
    if lang is None:
        lang = get_current_language()
    translation = translations.get(lang, translations['en']).get(key, translations['en'].get(key, key))
    if kwargs:
        try:
            return translation.format(**kwargs)
        except (KeyError, IndexError):
            return translation
    return translation

def init_session_state():
    if 'language' not in st.session_state:
        st.session_state.language = 'en'

def change_language(lang):
    st.session_state.language = lang

def get_current_language():
    return st.session_state.get('language', 'en')