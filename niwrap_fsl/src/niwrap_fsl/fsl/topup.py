# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TOPUP_METADATA = Metadata(
    id="1ce5f6bc3fb7d10100e8df605e624bdb9818a6d3.boutiques",
    name="topup",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


TopupParameters = typing.TypedDict('TopupParameters', {
    "__STYXTYPE__": typing.Literal["topup"],
    "imain": InputPathType,
    "datain": InputPathType,
    "out": typing.NotRequired[str | None],
    "fout": typing.NotRequired[str | None],
    "iout": typing.NotRequired[str | None],
    "logout": typing.NotRequired[str | None],
    "warpres": typing.NotRequired[float | None],
    "subsamp": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
    "config": typing.NotRequired[InputPathType | None],
    "miter": typing.NotRequired[float | None],
    "lambda": typing.NotRequired[float | None],
    "ssqlambda": bool,
    "regmod": typing.NotRequired[typing.Literal["membrane_energy", "bending_energy"] | None],
    "estmov": bool,
    "minmet": typing.NotRequired[typing.Literal[0, 1] | None],
    "splineorder": typing.NotRequired[typing.Literal[2, 3] | None],
    "numprec": typing.NotRequired[typing.Literal["double", "float"] | None],
    "interp": typing.NotRequired[typing.Literal["linear", "spline"] | None],
    "scale": bool,
    "regrid": bool,
    "nthr": typing.NotRequired[float | None],
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
        "topup": topup_cargs,
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
        "topup": topup_outputs,
    }.get(t)


class TopupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `topup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fieldcoef: OutputPathType | None
    """Spline coefficient field estimates (Hz)"""
    movpar: OutputPathType | None
    """Movement parameters"""
    fout: OutputPathType | None
    """Image file with field (Hz)"""
    iout: OutputPathType | None
    """4D image file with unwarped images"""
    logout: OutputPathType | None
    """Log file"""


def topup_params(
    imain: InputPathType,
    datain: InputPathType,
    out: str | None = None,
    fout: str | None = None,
    iout: str | None = None,
    logout: str | None = None,
    warpres: float | None = None,
    subsamp: float | None = None,
    fwhm: float | None = None,
    config: InputPathType | None = None,
    miter: float | None = None,
    lambda_: float | None = None,
    ssqlambda: bool = False,
    regmod: typing.Literal["membrane_energy", "bending_energy"] | None = None,
    estmov: bool = False,
    minmet: typing.Literal[0, 1] | None = None,
    splineorder: typing.Literal[2, 3] | None = None,
    numprec: typing.Literal["double", "float"] | None = None,
    interp: typing.Literal["linear", "spline"] | None = None,
    scale: bool = False,
    regrid: bool = False,
    nthr: float | None = None,
    verbose: bool = False,
) -> TopupParameters:
    """
    Build parameters.
    
    Args:
        imain: Name of 4D file with images.
        datain: Name of text file with PE directions/times.
        out: Base-name of output files (spline coefficients (Hz) and movement\
            parameters).
        fout: Name of image file with field (Hz).
        iout: Name of 4D image file with unwarped images.
        logout: Name of log-file.
        warpres: (Approximate) resolution (in mm) of warp basis for the\
            different sub-sampling levels, default 10.
        subsamp: Sub-sampling scheme, default 1.
        fwhm: FWHM (in mm) of gaussian smoothing kernel, default 8.
        config: Name of config file specifying command line arguments.
        miter: Max # of non-linear iterations, default 5.
        lambda_: Weight of regularisation, default depending on --ssqlambda and\
            --regmod switches. See user documentation.
        ssqlambda: If set (=1), lambda is weighted by current ssq, default 1.
        regmod: Model for regularisation of warp-field [membrane_energy\
            bending_energy], default bending_energy.
        estmov: Estimate movements if set, default 1 (true).
        minmet: Minimisation method 0=Levenberg-Marquardt, 1=Scaled Conjugate\
            Gradient, default 0 (LM).
        splineorder: Order of spline, 2=Quadratic spline, 3=Cubic spline.\
            Default=3.
        numprec: Precision for representing Hessian, double or float. Default\
            double.
        interp: Image interpolation model, linear or spline. Default spline.
        scale: If set (=1), the images are individually scaled to a common\
            mean, default 0 (false).
        regrid: If set (=1), the calculations are done in a different grid,\
            default 1 (true).
        nthr: Number of threads to use (cannot be greater than numbers of\
            hardware cores), default 1.
        verbose: Print diagnostic information while running.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "topup",
        "imain": imain,
        "datain": datain,
        "ssqlambda": ssqlambda,
        "estmov": estmov,
        "scale": scale,
        "regrid": regrid,
        "verbose": verbose,
    }
    if out is not None:
        params["out"] = out
    if fout is not None:
        params["fout"] = fout
    if iout is not None:
        params["iout"] = iout
    if logout is not None:
        params["logout"] = logout
    if warpres is not None:
        params["warpres"] = warpres
    if subsamp is not None:
        params["subsamp"] = subsamp
    if fwhm is not None:
        params["fwhm"] = fwhm
    if config is not None:
        params["config"] = config
    if miter is not None:
        params["miter"] = miter
    if lambda_ is not None:
        params["lambda"] = lambda_
    if regmod is not None:
        params["regmod"] = regmod
    if minmet is not None:
        params["minmet"] = minmet
    if splineorder is not None:
        params["splineorder"] = splineorder
    if numprec is not None:
        params["numprec"] = numprec
    if interp is not None:
        params["interp"] = interp
    if nthr is not None:
        params["nthr"] = nthr
    return params


def topup_cargs(
    params: TopupParameters,
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
    cargs.append("topup")
    cargs.append("--imain=" + execution.input_file(params.get("imain")))
    cargs.append("--datain=" + execution.input_file(params.get("datain")))
    if params.get("out") is not None:
        cargs.append("--out=" + params.get("out"))
    if params.get("fout") is not None:
        cargs.append("--fout=" + params.get("fout"))
    if params.get("iout") is not None:
        cargs.append("--iout=" + params.get("iout"))
    if params.get("logout") is not None:
        cargs.append("--logout=" + params.get("logout"))
    if params.get("warpres") is not None:
        cargs.append("--warpres=" + str(params.get("warpres")))
    if params.get("subsamp") is not None:
        cargs.append("--subsamp=" + str(params.get("subsamp")))
    if params.get("fwhm") is not None:
        cargs.append("--fwhm=" + str(params.get("fwhm")))
    if params.get("config") is not None:
        cargs.append("--config=" + execution.input_file(params.get("config")))
    if params.get("miter") is not None:
        cargs.append("--miter=" + str(params.get("miter")))
    if params.get("lambda") is not None:
        cargs.append("--lambda=" + str(params.get("lambda")))
    if params.get("ssqlambda"):
        cargs.append("--ssqlambda")
    if params.get("regmod") is not None:
        cargs.append("--regmod=" + params.get("regmod"))
    if params.get("estmov"):
        cargs.append("--estmov")
    if params.get("minmet") is not None:
        cargs.append("--minmet=" + str(params.get("minmet")))
    if params.get("splineorder") is not None:
        cargs.append("--splineorder=" + str(params.get("splineorder")))
    if params.get("numprec") is not None:
        cargs.append("--numprec=" + params.get("numprec"))
    if params.get("interp") is not None:
        cargs.append("--interp=" + params.get("interp"))
    if params.get("scale"):
        cargs.append("--scale")
    if params.get("regrid"):
        cargs.append("--regrid")
    if params.get("nthr") is not None:
        cargs.append("--nthr=" + str(params.get("nthr")))
    if params.get("verbose"):
        cargs.append("--verbose")
    return cargs


def topup_outputs(
    params: TopupParameters,
    execution: Execution,
) -> TopupOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TopupOutputs(
        root=execution.output_file("."),
        fieldcoef=execution.output_file(params.get("out") + "_fieldcoef.nii.gz") if (params.get("out") is not None) else None,
        movpar=execution.output_file(params.get("out") + "_movpar.txt") if (params.get("out") is not None) else None,
        fout=execution.output_file(params.get("fout")) if (params.get("fout") is not None) else None,
        iout=execution.output_file(params.get("iout")) if (params.get("iout") is not None) else None,
        logout=execution.output_file(params.get("logout")) if (params.get("logout") is not None) else None,
    )
    return ret


def topup_execute(
    params: TopupParameters,
    execution: Execution,
) -> TopupOutputs:
    """
    topup is part of FSL and is used to estimate and correct for
    susceptibility-induced distortions in echo planar imaging (EPI) data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TopupOutputs`).
    """
    params = execution.params(params)
    cargs = topup_cargs(params, execution)
    ret = topup_outputs(params, execution)
    execution.run(cargs)
    return ret


def topup(
    imain: InputPathType,
    datain: InputPathType,
    out: str | None = None,
    fout: str | None = None,
    iout: str | None = None,
    logout: str | None = None,
    warpres: float | None = None,
    subsamp: float | None = None,
    fwhm: float | None = None,
    config: InputPathType | None = None,
    miter: float | None = None,
    lambda_: float | None = None,
    ssqlambda: bool = False,
    regmod: typing.Literal["membrane_energy", "bending_energy"] | None = None,
    estmov: bool = False,
    minmet: typing.Literal[0, 1] | None = None,
    splineorder: typing.Literal[2, 3] | None = None,
    numprec: typing.Literal["double", "float"] | None = None,
    interp: typing.Literal["linear", "spline"] | None = None,
    scale: bool = False,
    regrid: bool = False,
    nthr: float | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> TopupOutputs:
    """
    topup is part of FSL and is used to estimate and correct for
    susceptibility-induced distortions in echo planar imaging (EPI) data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        imain: Name of 4D file with images.
        datain: Name of text file with PE directions/times.
        out: Base-name of output files (spline coefficients (Hz) and movement\
            parameters).
        fout: Name of image file with field (Hz).
        iout: Name of 4D image file with unwarped images.
        logout: Name of log-file.
        warpres: (Approximate) resolution (in mm) of warp basis for the\
            different sub-sampling levels, default 10.
        subsamp: Sub-sampling scheme, default 1.
        fwhm: FWHM (in mm) of gaussian smoothing kernel, default 8.
        config: Name of config file specifying command line arguments.
        miter: Max # of non-linear iterations, default 5.
        lambda_: Weight of regularisation, default depending on --ssqlambda and\
            --regmod switches. See user documentation.
        ssqlambda: If set (=1), lambda is weighted by current ssq, default 1.
        regmod: Model for regularisation of warp-field [membrane_energy\
            bending_energy], default bending_energy.
        estmov: Estimate movements if set, default 1 (true).
        minmet: Minimisation method 0=Levenberg-Marquardt, 1=Scaled Conjugate\
            Gradient, default 0 (LM).
        splineorder: Order of spline, 2=Quadratic spline, 3=Cubic spline.\
            Default=3.
        numprec: Precision for representing Hessian, double or float. Default\
            double.
        interp: Image interpolation model, linear or spline. Default spline.
        scale: If set (=1), the images are individually scaled to a common\
            mean, default 0 (false).
        regrid: If set (=1), the calculations are done in a different grid,\
            default 1 (true).
        nthr: Number of threads to use (cannot be greater than numbers of\
            hardware cores), default 1.
        verbose: Print diagnostic information while running.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TopupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TOPUP_METADATA)
    params = topup_params(
        imain=imain,
        datain=datain,
        out=out,
        fout=fout,
        iout=iout,
        logout=logout,
        warpres=warpres,
        subsamp=subsamp,
        fwhm=fwhm,
        config=config,
        miter=miter,
        lambda_=lambda_,
        ssqlambda=ssqlambda,
        regmod=regmod,
        estmov=estmov,
        minmet=minmet,
        splineorder=splineorder,
        numprec=numprec,
        interp=interp,
        scale=scale,
        regrid=regrid,
        nthr=nthr,
        verbose=verbose,
    )
    return topup_execute(params, execution)


__all__ = [
    "TOPUP_METADATA",
    "TopupOutputs",
    "TopupParameters",
    "topup",
    "topup_params",
]
