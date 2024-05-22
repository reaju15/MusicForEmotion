# MusicForEmotion: A Web App for Emotion-Based Music Recommendations

## Overview

MusicEmotion is a web application designed to provide music recommendations based on your current emotional state. By analyzing user input about their feelings, MusicEmotion offers a personalized playlist that resonates with their mood, helping to enhance or alleviate their emotions through the power of music.

## Features

- **Emotion Analysis**: Users can select or input their current emotions.
- **Personalized Playlists**: Generate music playlists tailored to the user's emotional state.
- **Mood Tracking**: Keep a history of emotions and music preferences to refine recommendations.
- **Integration with Music Services**: Connect with popular music streaming services (e.g., Spotify, Apple Music) for seamless playback.
- **User Profiles**: Create and manage user profiles to save preferences and playlists.
- **Responsive Design**: Accessible on both desktop and mobile devices.

## Getting Started

### Prerequisites

To run MusicEmotion locally, ensure you have the following installed:

- Node.js (v14.0.0 or higher)
- npm (v6.0.0 or higher)
- Spotify music streaming service account

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/reaju15/musicforemotion.git
   cd musicforemotion
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your API keys and necessary configuration. For example:
     ```plaintext
     SPOTIFY_CLIENT_ID=your_spotify_client_id
     SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
     ```

4. Run the application:
   ```bash
   npm start
   ```

5. Open your web browser and go to `http://localhost:3000`.

### Usage

1. **Log In**: Create an account or log in using your credentials.
2. **Select Emotion**: Choose your current emotion from the provided options or enter it manually.
3. **Get Playlist**: Click the "Generate Playlist" button to receive a curated list of songs that match your mood.
4. **Play Music**: Connect to your preferred music streaming service and enjoy your personalized playlist.

