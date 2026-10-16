// BB Fitness Crew - Theme Manager
(function () {
    "use strict";

    function initTheme() {
        var button = document.getElementById("theme-toggle");
        var label = document.getElementById("theme-label");
        var root = document.documentElement;

        function applyTheme(theme) {
            root.setAttribute("data-theme", theme);

            if (button) {
                var isLight = theme === "light";
                button.setAttribute("aria-checked", isLight ? "true" : "false");
                button.setAttribute(
                    "aria-label",
                    isLight ? "Switch to dark mode" : "Switch to light mode"
                );
                button.title = "Current: " + (isLight ? "Light Mode" : "Dark Mode") + ". Click to switch.";
            }

            if (label) {
                label.textContent = theme === "light" ? "Light" : "Dark";
            }
        }

        var savedTheme = "dark";
        try {
            var local = localStorage.getItem("gym-theme");
            if (local === "light" || local === "dark") {
                savedTheme = local;
            } else if (root.getAttribute("data-theme")) {
                savedTheme = root.getAttribute("data-theme");
            }
        } catch (e) {
            savedTheme = "dark";
        }

        applyTheme(savedTheme);

        if (button) {
            button.addEventListener("click", function () {
                var currentTheme = root.getAttribute("data-theme") || "dark";
                var nextTheme = currentTheme === "dark" ? "light" : "dark";

                applyTheme(nextTheme);

                try {
                    localStorage.setItem("gym-theme", nextTheme);
                } catch (e) {
                    console.warn("Theme preference could not be saved to localStorage.", e);
                }
            });
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initTheme);
    } else {
        initTheme();
    }
})();
