# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RBA_METADATA = Metadata(
    id="180fca902f5ffecfd9602bea793e87295168a52b.boutiques",
    name="RBA",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


RbaParameters = typing.TypedDict('RbaParameters', {
    "__STYXTYPE__": typing.Literal["RBA"],
    "prefix": str,
    "dataTable": InputPathType,
    "chains": typing.NotRequired[float | None],
    "iterations": typing.NotRequired[float | None],
    "model": typing.NotRequired[str | None],
    "eoi": typing.NotRequired[str | None],
    "wcp": typing.NotRequired[float | None],
    "tstat": typing.NotRequired[str | None],
    "stdz": typing.NotRequired[str | None],
    "cVars": typing.NotRequired[str | None],
    "qVars": typing.NotRequired[str | None],
    "distROI": typing.NotRequired[str | None],
    "distSubj": typing.NotRequired[str | None],
    "distY": typing.NotRequired[str | None],
    "ridgePlot": typing.NotRequired[str | None],
    "roi": typing.NotRequired[str | None],
    "subj": typing.NotRequired[str | None],
    "scale": typing.NotRequired[float | None],
    "se": typing.NotRequired[str | None],
    "pdp": typing.NotRequired[str | None],
    "mean": typing.NotRequired[str | None],
    "sigma": typing.NotRequired[str | None],
    "debug": bool,
    "verbose": typing.NotRequired[float | None],
    "md": bool,
    "r2z": bool,
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
        "RBA": rba_cargs,
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
        "RBA": rba_outputs,
    }.get(t)


class RbaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rba(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_txt: OutputPathType
    """Main output text file with inference information for effects of
    interest."""
    output_rdata: OutputPathType
    """Saved R data in binary format for post hoc processing."""


def rba_params(
    prefix: str,
    data_table: InputPathType,
    chains: float | None = None,
    iterations: float | None = None,
    model: str | None = None,
    eoi: str | None = None,
    wcp: float | None = None,
    tstat: str | None = None,
    stdz: str | None = None,
    c_vars: str | None = None,
    q_vars: str | None = None,
    dist_roi: str | None = None,
    dist_subj: str | None = None,
    dist_y: str | None = None,
    ridge_plot: str | None = None,
    roi: str | None = None,
    subj: str | None = None,
    scale: float | None = None,
    se: str | None = None,
    pdp: str | None = None,
    mean: str | None = None,
    sigma: str | None = None,
    debug: bool = False,
    verbose: float | None = None,
    md: bool = False,
    r2z: bool = False,
) -> RbaParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix for output file names.
        data_table: Data table in pure text format.
        chains: Specify the number of Markov chains.
        iterations: Specify the number of iterations per Markov chain.
        model: Specify the model formula.
        eoi: Identify effects of interest in the output.
        wcp: Invoke within-chain parallelization.
        tstat: Specify the column name that lists the t-statistic values.
        stdz: Identify quantitative variables (or covariates) to be\
            standardized.
        c_vars: Identify categorical (qualitative) variables (or factors).
        q_vars: Identify quantitative variables (or covariates).
        dist_roi: Specify the distribution for the ROIs.
        dist_subj: Specify the distribution for the subjects.
        dist_y: Specify the distribution for the response variable.
        ridge_plot: Plot the posterior distributions stacked together.
        roi: Specify the column name that is designated as the region variable.
        subj: Specify the column name that is designated as the measuring unit\
            variable (usually subject).
        scale: Specify a multiplier for the Y values.
        se: This option indicates that standard error for the response variable\
            is available as input.
        pdp: Specify the layout of posterior distribution plot.
        mean: Specify the formulation for the mean of the likelihood (sampling\
            distribution).
        sigma: Specify the formulation for the standard deviation (sigma) of\
            the likelihood (sampling distribution).
        debug: This option will enable R to save the parameters in a file for\
            debugging.
        verbose: Specify verbose level.
        md: This option indicates that there are missing data in the input.
        r2z: Perform Fisher transformation on the response variable if it is a\
            correlation coefficient.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "RBA",
        "prefix": prefix,
        "dataTable": data_table,
        "debug": debug,
        "md": md,
        "r2z": r2z,
    }
    if chains is not None:
        params["chains"] = chains
    if iterations is not None:
        params["iterations"] = iterations
    if model is not None:
        params["model"] = model
    if eoi is not None:
        params["eoi"] = eoi
    if wcp is not None:
        params["wcp"] = wcp
    if tstat is not None:
        params["tstat"] = tstat
    if stdz is not None:
        params["stdz"] = stdz
    if c_vars is not None:
        params["cVars"] = c_vars
    if q_vars is not None:
        params["qVars"] = q_vars
    if dist_roi is not None:
        params["distROI"] = dist_roi
    if dist_subj is not None:
        params["distSubj"] = dist_subj
    if dist_y is not None:
        params["distY"] = dist_y
    if ridge_plot is not None:
        params["ridgePlot"] = ridge_plot
    if roi is not None:
        params["roi"] = roi
    if subj is not None:
        params["subj"] = subj
    if scale is not None:
        params["scale"] = scale
    if se is not None:
        params["se"] = se
    if pdp is not None:
        params["pdp"] = pdp
    if mean is not None:
        params["mean"] = mean
    if sigma is not None:
        params["sigma"] = sigma
    if verbose is not None:
        params["verbose"] = verbose
    return params


def rba_cargs(
    params: RbaParameters,
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
    cargs.append("RBA")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.extend([
        "-dataTable",
        execution.input_file(params.get("dataTable"))
    ])
    if params.get("chains") is not None:
        cargs.extend([
            "-chains",
            str(params.get("chains"))
        ])
    if params.get("iterations") is not None:
        cargs.extend([
            "-iterations",
            str(params.get("iterations"))
        ])
    if params.get("model") is not None:
        cargs.extend([
            "-model",
            params.get("model")
        ])
    if params.get("eoi") is not None:
        cargs.extend([
            "-EOI",
            params.get("eoi")
        ])
    if params.get("wcp") is not None:
        cargs.extend([
            "-WCP",
            str(params.get("wcp"))
        ])
    if params.get("tstat") is not None:
        cargs.extend([
            "-tstat",
            params.get("tstat")
        ])
    if params.get("stdz") is not None:
        cargs.extend([
            "-stdz",
            params.get("stdz")
        ])
    if params.get("cVars") is not None:
        cargs.extend([
            "-cVars",
            params.get("cVars")
        ])
    if params.get("qVars") is not None:
        cargs.extend([
            "-qVars",
            params.get("qVars")
        ])
    if params.get("distROI") is not None:
        cargs.extend([
            "-distROI",
            params.get("distROI")
        ])
    if params.get("distSubj") is not None:
        cargs.extend([
            "-distSubj",
            params.get("distSubj")
        ])
    if params.get("distY") is not None:
        cargs.extend([
            "-distY",
            params.get("distY")
        ])
    if params.get("ridgePlot") is not None:
        cargs.extend([
            "-ridgePlot",
            params.get("ridgePlot")
        ])
    if params.get("roi") is not None:
        cargs.extend([
            "-ROI",
            params.get("roi")
        ])
    if params.get("subj") is not None:
        cargs.extend([
            "-Subj",
            params.get("subj")
        ])
    if params.get("scale") is not None:
        cargs.extend([
            "-scale",
            str(params.get("scale"))
        ])
    if params.get("se") is not None:
        cargs.extend([
            "-se",
            params.get("se")
        ])
    if params.get("pdp") is not None:
        cargs.extend([
            "-PDP",
            params.get("pdp")
        ])
    if params.get("mean") is not None:
        cargs.extend([
            "-mean",
            params.get("mean")
        ])
    if params.get("sigma") is not None:
        cargs.extend([
            "-sigma",
            params.get("sigma")
        ])
    if params.get("debug"):
        cargs.append("-dbgArgs")
    if params.get("verbose") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbose"))
        ])
    if params.get("md"):
        cargs.append("-MD")
    if params.get("r2z"):
        cargs.append("-r2z")
    return cargs


def rba_outputs(
    params: RbaParameters,
    execution: Execution,
) -> RbaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RbaOutputs(
        root=execution.output_file("."),
        output_txt=execution.output_file(params.get("prefix") + ".txt"),
        output_rdata=execution.output_file(params.get("prefix") + ".RData"),
    )
    return ret


def rba_execute(
    params: RbaParameters,
    execution: Execution,
) -> RbaOutputs:
    """
    Region-Based Analysis Program through Bayesian Multilevel Modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RbaOutputs`).
    """
    params = execution.params(params)
    cargs = rba_cargs(params, execution)
    ret = rba_outputs(params, execution)
    execution.run(cargs)
    return ret


def rba(
    prefix: str,
    data_table: InputPathType,
    chains: float | None = None,
    iterations: float | None = None,
    model: str | None = None,
    eoi: str | None = None,
    wcp: float | None = None,
    tstat: str | None = None,
    stdz: str | None = None,
    c_vars: str | None = None,
    q_vars: str | None = None,
    dist_roi: str | None = None,
    dist_subj: str | None = None,
    dist_y: str | None = None,
    ridge_plot: str | None = None,
    roi: str | None = None,
    subj: str | None = None,
    scale: float | None = None,
    se: str | None = None,
    pdp: str | None = None,
    mean: str | None = None,
    sigma: str | None = None,
    debug: bool = False,
    verbose: float | None = None,
    md: bool = False,
    r2z: bool = False,
    runner: Runner | None = None,
) -> RbaOutputs:
    """
    Region-Based Analysis Program through Bayesian Multilevel Modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for output file names.
        data_table: Data table in pure text format.
        chains: Specify the number of Markov chains.
        iterations: Specify the number of iterations per Markov chain.
        model: Specify the model formula.
        eoi: Identify effects of interest in the output.
        wcp: Invoke within-chain parallelization.
        tstat: Specify the column name that lists the t-statistic values.
        stdz: Identify quantitative variables (or covariates) to be\
            standardized.
        c_vars: Identify categorical (qualitative) variables (or factors).
        q_vars: Identify quantitative variables (or covariates).
        dist_roi: Specify the distribution for the ROIs.
        dist_subj: Specify the distribution for the subjects.
        dist_y: Specify the distribution for the response variable.
        ridge_plot: Plot the posterior distributions stacked together.
        roi: Specify the column name that is designated as the region variable.
        subj: Specify the column name that is designated as the measuring unit\
            variable (usually subject).
        scale: Specify a multiplier for the Y values.
        se: This option indicates that standard error for the response variable\
            is available as input.
        pdp: Specify the layout of posterior distribution plot.
        mean: Specify the formulation for the mean of the likelihood (sampling\
            distribution).
        sigma: Specify the formulation for the standard deviation (sigma) of\
            the likelihood (sampling distribution).
        debug: This option will enable R to save the parameters in a file for\
            debugging.
        verbose: Specify verbose level.
        md: This option indicates that there are missing data in the input.
        r2z: Perform Fisher transformation on the response variable if it is a\
            correlation coefficient.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RbaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RBA_METADATA)
    params = rba_params(
        prefix=prefix,
        data_table=data_table,
        chains=chains,
        iterations=iterations,
        model=model,
        eoi=eoi,
        wcp=wcp,
        tstat=tstat,
        stdz=stdz,
        c_vars=c_vars,
        q_vars=q_vars,
        dist_roi=dist_roi,
        dist_subj=dist_subj,
        dist_y=dist_y,
        ridge_plot=ridge_plot,
        roi=roi,
        subj=subj,
        scale=scale,
        se=se,
        pdp=pdp,
        mean=mean,
        sigma=sigma,
        debug=debug,
        verbose=verbose,
        md=md,
        r2z=r2z,
    )
    return rba_execute(params, execution)


__all__ = [
    "RBA_METADATA",
    "RbaOutputs",
    "RbaParameters",
    "rba",
    "rba_params",
]
