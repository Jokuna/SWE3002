package com.example.dormie

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.JsResult
import android.webkit.WebChromeClient
import android.webkit.WebResourceRequest
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.appcompat.app.AlertDialog

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val webView: WebView = findViewById(R.id.webview)

        // url 설정
        val url = "https://swe3002.jokuna.dev/"

        webView.settings.javaScriptEnabled = true
        webView.settings.domStorageEnabled = true

        // ZOOM 비활성화
        webView.settings.setSupportZoom(false)
        webView.settings.builtInZoomControls = false
        webView.settings.displayZoomControls = false

        webView.settings.useWideViewPort = true
        webView.settings.loadWithOverviewMode = true

        // text scale 100% 고정
        webView.settings.textZoom = 100

        // scale 100%
        // webView.setInitialScale(1)

        // webView: alert 설정
        webView.webChromeClient = object : WebChromeClient() {
            override fun onJsAlert(view: WebView, url: String, message: String, result: JsResult): Boolean {
                // 여기에 alert을 처리하는 코드를 추가

                AlertDialog.Builder(this@MainActivity)
                    .setMessage(message)
                    .setPositiveButton(android.R.string.ok) { dialog, which ->
                        result?.confirm()
                    }
                    .setCancelable(false)
                    .create()
                    .show()
                return true
            }

            // 필요한 다른 메서드들을 여기에 오버라이드
        }

        // 링크가 WebView 내에서 열리도록 설정
        webView.webViewClient = object : WebViewClient() {
            override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
                view.loadUrl(request.url.toString())
                return true
            }
        }

        webView.loadUrl(url)
    }

}