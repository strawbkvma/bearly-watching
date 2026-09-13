# I Have 10 Minutes 🍓🌷

> An iOS app for making the most of the little moments you have.

**I Have 10 Minutes** is a simple SwiftUI app that helps you find small activities based on how much time you have and what you need right now.

Whether you want to rest, focus, have fun, or get something done, the app gives you a small and manageable activity to start with.

Everything is designed to feel simple, gentle, and easy to use. 🌷

---

## ✨ Features

* ⏱️ Choose how much time you have
* 🌿 Get gentle activity suggestions
* 🛌 Rest activities
* 🧠 Focus activities
* 🎨 Fun and creative activities
* ✅ Small productivity activities
* 💭 View activity details and steps
* ▶️ Start an activity timer
* 📖 Track completed activities in History
* 👤 Personalize your name
* 🏠 Simple tab-based navigation
* 🎨 Soft pastel and minimal interface
* 📱 Built entirely with SwiftUI

---

## 🛠️ Requirements

Before running the app, make sure you have:

* macOS
* Xcode
* iOS Simulator or a compatible iPhone
* Swift / SwiftUI

---

## 🍓 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/strawbkvma/IHave10Minutes.git
cd IHave10Minutes
```

### 2. Open the project

Open:

```text
IHave10Minutes.xcodeproj
```

with Xcode.

### 3. Run the app

Select an iOS Simulator or connected iPhone, then press:

**Run ▶︎**

That's it. 🍓

---

## 🌷 How It Works

I Have 10 Minutes is built around one simple question:

> **What do you need right now?**

Choose how much time you have, then pick what you feel like doing.

```text
How much time do you have?
            ↓
      Choose a time
            ↓
       What do you need?
            ↓
   ┌────────┼────────┐
   ↓        ↓        ↓
  Rest    Focus    Have Fun
            │
            ↓
     Get Things Done
            ↓
      Gentle Activity
            ↓
         Start Timer
```

---

## ⏱️ Time Options

The app provides different activity durations:

| Time   | Example              |
| ------ | -------------------- |
| 5 min  | Reply to One Message |
| 10 min | Stretch & Breathe    |
| 20 min | Slow Walk            |
| 30 min | Longer activities    |

The available activities are designed to match the amount of time you have.

---

## 🌿 Activity Categories

### 🛌 Rest

Small activities for slowing down and recharging.

Examples:

* Stretch & Breathe
* Mindful Tea
* Window Reset
* Slow Walk

---

### 🧠 Focus

Activities designed to help clear your mind and regain focus.

Examples:

* Desk Reset
* Brain Dump
* One Tiny Task
* Breathe & Refocus

---

### 🎨 Have Fun

Small creative or playful activities for taking a break.

Examples:

* Doodle Something
* Tiny Creative Break
* Something Silly
* Play a Little

---

### ✅ Get Things Done

Small tasks that help you make progress without feeling overwhelming.

Examples:

* Reply to One Message
* Quick Desk Organization
* Clear One Tiny Task
* Make a Tiny Plan

---

## 💭 Activity Details

Each activity includes:

* Category
* Duration
* Activity title
* Short description
* Step-by-step instructions

Example:

```text
REST · 10 min

Stretch & Breathe

A small reset for your body and mind.

1. Find a comfortable position
2. Stretch gently
3. Take a few slow breaths
4. Let your shoulders relax
```

---

## ⏳ Activity Timer

Once an activity is selected, you can start a timer based on its duration.

The timer supports:

* ▶️ Starting an activity
* ⏱️ Countdown timer
* 🏁 Completing an activity
* 🏠 Returning home after the session

Completed activities are saved to your local history.

Ending a session early does **not** add it to History.

---

## 📖 History

The History screen keeps track of activities you have completed.

It allows you to look back at the small things you've taken time to do.

Activity history is stored locally using:

```text
UserDefaults
```

No external database is required.

---

## 👤 Profile

The Profile screen lets you personalize your experience.

You can set your name and have the Home screen automatically update the greeting.

For example:

```text
Good morning, Alex
```

Your name is stored locally using:

```text
@AppStorage
```

---

## 🧸 Navigation

The app uses a simple three-tab navigation:

```text
┌──────────┬──────────┬──────────┐
│   Home   │ History  │ Profile  │
└──────────┴──────────┴──────────┘
```

Activities are presented through a simple flow:

```text
Home
 ↓
Need
 ↓
Gentle Idea
 ↓
Activity Details
 ↓
Timer
 ↓
Home
```

---

## 🛠️ Tech Stack

* **Swift**
* **SwiftUI**
* **Xcode**
* **UserDefaults**
* **AppStorage**

The app uses SwiftUI's navigation and state management to keep the interface lightweight and responsive.

---

## 📁 Project Structure

```text
IHave10Minutes/
│
├── IHave10Minutes.xcodeproj
│
├── IHave10Minutes/
│   ├── ActivityDetailView.swift
│   ├── AppTheme.swift
│   ├── BottomNavigation.swift
│   ├── ContentView.swift
│   ├── GentleIdeaView.swift
│   ├── HistoryStore.swift
│   ├── HistoryView.swift
│   ├── HomeView.swift
│   ├── IHave10MinutesApp.swift
│   ├── MainView.swift
│   ├── NeedView.swift
│   ├── ProfileView.swift
│   ├── SplashView.swift
│   ├── TimeCard.swift
│   └── TimerView.swift
│
├── README.md
├── LICENSE
└── .gitignore
```

### Main Files

#### `HomeView.swift`

Displays the greeting, available time options, and the main starting point of the app.

#### `NeedView.swift`

Allows users to choose what they currently need:

* Rest
* Focus
* Have Fun
* Get Things Done

#### `GentleIdeaView.swift`

Contains the activity suggestions and activity information.

#### `ActivityDetailView.swift`

Displays detailed information and steps for the selected activity.

#### `TimerView.swift`

Handles the activity countdown timer and completion flow.

#### `HistoryStore.swift`

Stores and retrieves completed activities using `UserDefaults`.

#### `ProfileView.swift`

Handles the user's name and profile customization.

#### `MainView.swift`

Controls the main tab navigation between Home, History, and Profile.

---

## 🔒 Privacy

I Have 10 Minutes is designed as a local-first app.

It does **not**:

* require an account
* require a backend
* send activity history to a server
* store personal information remotely
* require an internet connection for the core experience

Your name and activity history are stored locally on the device.

---

## 🏗️ Architecture

```text
┌──────────────────────┐
│      SwiftUI App     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       MainView       │
│                      │
│ Home / History /     │
│ Profile              │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Activity Flow     │
│                      │
│ Need → Idea → Detail │
│        → Timer       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Local Storage     │
│                      │
│ UserDefaults         │
│ AppStorage            │
└──────────────────────┘
```

---

## 🐛 Troubleshooting

### The app doesn't build

Make sure:

1. You are using a compatible version of Xcode.
2. The correct iOS Simulator is selected.
3. The project is opened through `IHave10Minutes.xcodeproj`.
4. All Swift files are included in the Xcode target.

---

### History isn't showing

Completed activities are stored locally.

Try:

1. Completing an activity instead of ending it early.
2. Restarting the app.
3. Running the app again on the same Simulator/device.

---

### The profile name doesn't update

The name is shared using:

```swift
@AppStorage("userName")
```

Make sure the app is running with the latest project files.

---

## 🗺️ Roadmap

### 🌷 Activities

* [x] Rest activities
* [x] Focus activities
* [x] Fun activities
* [x] Productivity activities
* [x] Activity instructions
* [ ] More activity suggestions
* [ ] More activity illustrations

### ⏳ Timer

* [x] Activity countdown
* [x] Early session ending
* [x] Completion handling
* [x] Return to Home after session

### 📖 History

* [x] Completed activity tracking
* [x] Local persistence
* [ ] Activity statistics
* [ ] Calendar-based history

### 👤 Personalization

* [x] Editable name
* [x] Local profile storage
* [ ] More personalization options

### 🎨 Future Improvements

* [ ] More polished animations
* [ ] More illustrations
* [ ] Accessibility improvements
* [ ] Expanded activity library

---

## 📜 License

I Have 10 Minutes is open-source software licensed under the **MIT License**.

See [`LICENSE`](https://github.com/strawbkvma/i-have-10-minutes/blob/main/LICENSE) for details.

---

## 🍓 About

**I Have 10 Minutes** started as a small iOS project exploring **SwiftUI, thoughtful interaction design, and tiny moments of everyday life**.

The idea is simple:

> You don't always need a lot of time to do something good for yourself. 🌷

Made with SwiftUI ♡
