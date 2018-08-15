FROM openjdk:8
ADD "http://www.eclipse.org/downloads/download.php?file=/mat/1.8/rcp/MemoryAnalyzer-1.8.0.20180604-linux.gtk.x86_64.zip&mirror_id=1" /mat.zip
RUN [ "unzip", "/mat.zip" ]
ADD mat_analysis.sh /
ENTRYPOINT [ "/mat_analysis.sh" ]
