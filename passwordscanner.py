import re

def password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif 8 <= len(password) <= 12:
        score += 1
        feedback.append("Password length is acceptable, but longer is better.")
    else:
        score += 2
        feedback.append("Good password length.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Use special characters (e.g., !, @, #) for added security.")

    # Check uniqueness
    if len(set(password)) < len(password) * 0.7:
        feedback.append("Avoid using repeated characters or predictable patterns.")
    else:
        score += 1

    # Final score
    if score >= 7:
        return "Strong", feedback
    elif 4 <= score < 7:
        return "Moderate", feedback
    else:
        return "Weak", feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = password_strength(password)
    print(f"Password Strength: {strength}")
    print("\nSuggestions:")
    for tip in feedback:
        print(f"- {tip}")

if __name__ == "__main__":
    main()
