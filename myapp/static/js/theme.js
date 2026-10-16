
document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("theme-toggle");
    const icon = document.getElementById("theme-icon");
    const label = document.getElementById("theme-label");
    const root = document.documentElement;

    if (!button) {
        console.error("Theme toggle button not found!");
        return;
    }

    function applyTheme(theme) {
        root.setAttribute("data-theme", theme);

        if (icon) {
            icon.textContent = theme === "dark" ? "☀️" : "🌙";
        }

        if (label) {
            label.textContent =
                theme === "dark" ? "Light Mode" : "Dark Mode";
        }

        button.setAttribute(
            "aria-label",
            theme === "dark"
                ? "Switch to light mode"
                : "Switch to dark mode"
        );
    }

    let savedTheme;

    try {
        savedTheme = localStorage.getItem("gym-theme");
    } catch (error) {
        savedTheme = null;
    }

    applyTheme(
        savedTheme === "light" || savedTheme === "dark"
            ? savedTheme
            : "dark"
    );

    button.addEventListener("click", function () {
        const currentTheme = root.getAttribute("data-theme");
        const newTheme = currentTheme === "dark" ? "light" : "dark";

        applyTheme(newTheme);

        try {
            localStorage.setItem("gym-theme", newTheme);
        } catch (error) {
            console.warn("Theme preference could not be saved.");
        }

        console.log("Current theme:", newTheme);
    });
});
