# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

APQC_MAKE_HTML_METADATA = Metadata(
    id="a958dc9e454decaf99b430f63930ca86b1108a1f.boutiques",
    name="apqc_make_html",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


ApqcMakeHtmlParameters = typing.TypedDict('ApqcMakeHtmlParameters', {
    "__STYX_TYPE__": typing.Literal["apqc_make_html"],
    "qc_dir": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "apqc_make_html": apqc_make_html_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class ApqcMakeHtmlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apqc_make_html(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def apqc_make_html_params(
    qc_dir: str,
) -> ApqcMakeHtmlParameters:
    """
    Build parameters.
    
    Args:
        qc_dir: Directory where QC files will be saved.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "apqc_make_html",
        "qc_dir": qc_dir,
    }
    return params


def apqc_make_html_cargs(
    params: ApqcMakeHtmlParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("apqc_make_html.py")
    cargs.extend([
        "-qc_dir",
        params.get("qc_dir")
    ])
    return cargs


def apqc_make_html_outputs(
    params: ApqcMakeHtmlParameters,
    execution: Execution,
) -> ApqcMakeHtmlOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ApqcMakeHtmlOutputs(
        root=execution.output_file("."),
    )
    return ret


def apqc_make_html_execute(
    params: ApqcMakeHtmlParameters,
    execution: Execution,
) -> ApqcMakeHtmlOutputs:
    """
    Tool to generate HTML reports.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ApqcMakeHtmlOutputs`).
    """
    params = execution.params(params)
    cargs = apqc_make_html_cargs(params, execution)
    ret = apqc_make_html_outputs(params, execution)
    execution.run(cargs)
    return ret


def apqc_make_html(
    qc_dir: str,
    runner: Runner | None = None,
) -> ApqcMakeHtmlOutputs:
    """
    Tool to generate HTML reports.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        qc_dir: Directory where QC files will be saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApqcMakeHtmlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APQC_MAKE_HTML_METADATA)
    params = apqc_make_html_params(
        qc_dir=qc_dir,
    )
    return apqc_make_html_execute(params, execution)


__all__ = [
    "APQC_MAKE_HTML_METADATA",
    "ApqcMakeHtmlOutputs",
    "ApqcMakeHtmlParameters",
    "apqc_make_html",
    "apqc_make_html_params",
]
