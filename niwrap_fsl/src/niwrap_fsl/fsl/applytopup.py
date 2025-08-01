# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

APPLYTOPUP_METADATA = Metadata(
    id="15d02c2df08f23086cd22b7cf8555642b458a7f4.boutiques",
    name="applytopup",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ApplytopupParameters = typing.TypedDict('ApplytopupParameters', {
    "__STYXTYPE__": typing.Literal["applytopup"],
    "imain": list[InputPathType],
    "datain": InputPathType,
    "inindex": list[str],
    "topup": InputPathType,
    "out": str,
    "method": typing.NotRequired[typing.Literal["jac", "lsr"] | None],
    "interp": typing.NotRequired[typing.Literal["trilinear", "spline"] | None],
    "datatype": typing.NotRequired[typing.Literal["char", "short", "int", "float", "double"] | None],
    "verbose": bool,
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
        "applytopup": applytopup_cargs,
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
        "applytopup": applytopup_outputs,
    }.get(t)


class ApplytopupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `applytopup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output warped image."""


def applytopup_params(
    imain: list[InputPathType],
    datain: InputPathType,
    inindex: list[str],
    topup: InputPathType,
    out: str,
    method: typing.Literal["jac", "lsr"] | None = None,
    interp: typing.Literal["trilinear", "spline"] | None = None,
    datatype: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    verbose: bool = False,
) -> ApplytopupParameters:
    """
    Build parameters.
    
    Args:
        imain: Comma separated list of names of input image (to be corrected).
        datain: Name of text file with PE directions/times.
        inindex: Comma separated list of indices into --datain of the input\
            image (to be corrected).
        topup: Name of field/movements (from topup).
        out: Basename for output (warped) image.
        method: Use jacobian modulation (jac) or least-squares resampling\
            (lsr), default=lsr.
        interp: Interpolation method {trilinear, spline}, default=spline.
        datatype: Force output data type [char short int float double].
        verbose: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "applytopup",
        "imain": imain,
        "datain": datain,
        "inindex": inindex,
        "topup": topup,
        "out": out,
        "verbose": verbose,
    }
    if method is not None:
        params["method"] = method
    if interp is not None:
        params["interp"] = interp
    if datatype is not None:
        params["datatype"] = datatype
    return params


def applytopup_cargs(
    params: ApplytopupParameters,
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
    cargs.append("applytopup")
    cargs.append("--imain=" + ",".join([execution.input_file(f) for f in params.get("imain")]))
    cargs.append("--datain=" + execution.input_file(params.get("datain")))
    cargs.append("--inindex=" + ",".join(params.get("inindex")))
    cargs.append("--topup=" + execution.input_file(params.get("topup"), resolve_parent=True))
    cargs.append("--out=" + params.get("out"))
    if params.get("method") is not None:
        cargs.append("--method=" + params.get("method"))
    if params.get("interp") is not None:
        cargs.append("--interp=" + params.get("interp"))
    if params.get("datatype") is not None:
        cargs.append("--datatype=" + params.get("datatype"))
    if params.get("verbose"):
        cargs.append("--verbose")
    return cargs


def applytopup_outputs(
    params: ApplytopupParameters,
    execution: Execution,
) -> ApplytopupOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ApplytopupOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("out")),
    )
    return ret


def applytopup_execute(
    params: ApplytopupParameters,
    execution: Execution,
) -> ApplytopupOutputs:
    """
    applytopup applies corrections to images using the field estimates produced by
    topup.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ApplytopupOutputs`).
    """
    params = execution.params(params)
    cargs = applytopup_cargs(params, execution)
    ret = applytopup_outputs(params, execution)
    execution.run(cargs)
    return ret


def applytopup(
    imain: list[InputPathType],
    datain: InputPathType,
    inindex: list[str],
    topup: InputPathType,
    out: str,
    method: typing.Literal["jac", "lsr"] | None = None,
    interp: typing.Literal["trilinear", "spline"] | None = None,
    datatype: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> ApplytopupOutputs:
    """
    applytopup applies corrections to images using the field estimates produced by
    topup.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        imain: Comma separated list of names of input image (to be corrected).
        datain: Name of text file with PE directions/times.
        inindex: Comma separated list of indices into --datain of the input\
            image (to be corrected).
        topup: Name of field/movements (from topup).
        out: Basename for output (warped) image.
        method: Use jacobian modulation (jac) or least-squares resampling\
            (lsr), default=lsr.
        interp: Interpolation method {trilinear, spline}, default=spline.
        datatype: Force output data type [char short int float double].
        verbose: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApplytopupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APPLYTOPUP_METADATA)
    params = applytopup_params(
        imain=imain,
        datain=datain,
        inindex=inindex,
        topup=topup,
        out=out,
        method=method,
        interp=interp,
        datatype=datatype,
        verbose=verbose,
    )
    return applytopup_execute(params, execution)


__all__ = [
    "APPLYTOPUP_METADATA",
    "ApplytopupOutputs",
    "ApplytopupParameters",
    "applytopup",
    "applytopup_params",
]
