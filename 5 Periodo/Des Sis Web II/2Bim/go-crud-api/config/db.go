package config

import (
	"database/sql"
	"fmt"
	"log"
	"sync"

	_ "github.com/go-sql-driver/mysql"
)

const (
	DB_HOST     = "54.91.193.137"
	DB_USER     = "libertas"
	DB_PASSWORD = "123456"
	DB_NAME     = "libertas5per"
)

var (
	db   *sql.DB
	once sync.Once
)

func Connect() (*sql.DB, error) {
	var err error
	once.Do(func() {
		// Monta a string de conexão com timeout e parseTime
		dsn := fmt.Sprintf("%s:%s@tcp(%s)/%s?parseTime=true&timeout=5s&readTimeout=5s&writeTimeout=5s", DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

		db, err = sql.Open("mysql", dsn)
		if err != nil {
			return
		}

		db.SetMaxOpenConns(10)
		db.SetMaxIdleConns(5)
		db.SetConnMaxLifetime(0)

		log.Println("Connected to the database pool successfully!")
	})

	if err != nil {
		return nil, err
	}
	if db == nil {
		return nil, fmt.Errorf("database connection not initialized")
	}

	return db, nil
}

func Ping() error {
	if db == nil {
		return fmt.Errorf("database connection not initialized")
	}
	return db.Ping()
}

func CloseDB() error {
	if db != nil {
		return db.Close()
	}
	return nil
}
