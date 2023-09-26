import sqlite3


def setup_db():
    # create databank if not exists
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Create users table
    c.execute(
        """CREATE TABLE IF NOT EXISTS profile (
                        profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(100),
                        surname VARCHAR(60),
                        birthday DATE,
                        sex CHECK(sex IN ("male","female")) NOT NULL DEFAULT "male",
                        phone VARCHAR(100),
                        email VARCHAR(100),
                        email_pass VARCHAR(100),
                        address VARCHAR(200),
                        user_language VARCHAR(60) NOT NULL DEFAULT "english"
                    );"""
    )

    # Create templates table
    c.execute(
        """CREATE TABLE IF NOT EXISTS template (
                        template_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(250),
                        file VARCHAR(250),
                        type CHECK(type IN ("cv","letter")) NOT NULL DEFAULT "cv"
                    );"""
    )

    # Create experience table
    c.execute(
        """CREATE TABLE IF NOT EXISTS experience (
                        experience_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title VARCHAR(200),
                        description TEXT,
                        company VARCHAR(100),
                        date_start DATE,
                        date_end DATE,
                        profile_id INTEGER NOT NULL,
                        FOREIGN KEY(profile_id) REFERENCES profile(id) ON DELETE CASCADE
                    );"""
    )

    # Create education table
    c.execute(
        """CREATE TABLE IF NOT EXISTS education (
                        education_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title VARCHAR(200),
                        description TEXT,
                        school VARCHAR(100),
                        date_start DATE,
                        date_end DATE,
                        profile_id INTEGER NOT NULL,
                        FOREIGN KEY(profile_id) REFERENCES profile(id) ON DELETE CASCADE
                    );"""
    )

    # Create hobbies table
    c.execute(
        """CREATE TABLE IF NOT EXISTS hobby (
                        hobby_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        hobby VARCHAR(250),
                        profile_id INTEGER NOT NULL,
                        FOREIGN KEY(profile_id) REFERENCES profile(id) ON DELETE CASCADE
                    );"""
    )

    # Create skills table
    c.execute(
        """CREATE TABLE IF NOT EXISTS skill (
                        skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        skill VARCHAR(250),
                        profile_id INTEGER NOT NULL,
                        FOREIGN KEY(profile_id) REFERENCES profile(id) ON DELETE CASCADE
                    );"""
    )

    # Create applications table
    c.execute(
        """CREATE TABLE IF NOT EXISTS application (
                        application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        language VARCHAR(60) NOT NULL DEFAULT "english",
                        job_position VARCHAR(250),
                        job_description TEXT,
                        recuiter_name VARCHAR(100),
                        recuiter_surname VARCHAR(100),
                        recuiter_sex CHECK(recuiter_sex IN ("male","female","unknown")) NOT NULL DEFAULT "unknown",
                        recuiter_phone VARCHAR(100),
                        recuiter_email VARCHAR(200),
                        recuiter_address VARCHAR(200),
                        recuiter_atitude VARCHAR(60),
                        company_name VARCHAR(100),
                        company_address VARCHAR(200),
                        cv_summary TEXT,
                        letter_text TEXT,
                        file_cv VARCHAR(100),
                        file_letter VARCHAR(100),
                        date_creation DATETIME,
                        date_sending DATETIME,
                        template_id INTEGER NOT NULL,
                        profile_id INTEGER NOT NULL,
                        FOREIGN KEY(template_id) REFERENCES template(template_id) ON DELETE CASCADE,
                        FOREIGN KEY(profile_id) REFERENCES profile(profile_id) ON DELETE CASCADE
                    );"""
    )

    # Commit the changes
    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup_db()
